import pandas as pd
import gspread

import astreintes.models
import astreintes.calculs

FOLDER_ID = '18iaecTVG9ZDjGRDHsErAUJthK5ij6myV'


def create_or_get_sheet(
    wkb: gspread.spreadsheet.Spreadsheet, title: str, clear: bool = False, rows: int = 128, cols: int = 32
) -> gspread.Worksheet:
    """
    :param wkb:
    :param clear:
    :param rows:
    :param cols:
    :return:
    """
    wks = next((wk for wk in wkb.worksheets() if wk.title == title), None)
    if wks is None:
        wks = wkb.add_worksheet(title=title, rows=rows, cols=cols)
    else:
        if clear:
            wks.clear()
    return wks


class FeuilleAstreinte:
    def __init__(self, gc: gspread.Client, nom: str, folder_id: str = FOLDER_ID):
        self.gc = gc
        self.nom = nom
        self.folder_id = folder_id
        self.wkb = self.get_or_duplicate_workbook()

    def get_or_duplicate_workbook(self) -> gspread.Spreadsheet:
        files = self.gc.list_spreadsheet_files(folder_id=self.folder_id)
        key = next((f['id'] for f in files if f['name'] == self.nom), None)
        if key is None:
            wkb_template = self.gc.open('00_modèle')
            wkb = self.gc.copy(wkb_template.id, title=self.nom)
        else:
            wkb = self.gc.open_by_key(key)
        return wkb

    def set_values(self, df_sites, params):
        wks = self.wkb.worksheet('sites')
        wks.batch_clear(['A2:D8'])
        wks.update(df_sites.values.tolist(), 'A2')
        wks = self.wkb.worksheet('paramètres')
        wks.update([[int(v)] for v in params.model_dump().values()], 'B2')

    def calcul(self):
        df_sites = pd.DataFrame(self.wkb.worksheet('sites').get_all_records()).rename(
            columns={
                'Nom': 'nom',
                'Techniciens AGA': 'aga',
                'Techniciens Respi': 'respi',
                "Nombre minimum d'astreintes": 'rotations',
            }
        )
        params = self.wkb.worksheet('paramètres').get_all_records()
        params = {k: p['Donnée'] for k, p in zip(astreintes.models.Parametres.model_fields, params)}
        params = astreintes.models.Parametres(**params)
        r = astreintes.calculs.genere_planning(df_sites, params=params, mode='raise')
        df_planning, df_report_effectifs, df_report_sites, df_report_specialite, validation = r
        wks = create_or_get_sheet(self.wkb, 'planning', clear=True)
        wks.update([df_planning.columns.values.tolist()] + df_planning.values.tolist())
        wks = create_or_get_sheet(self.wkb, 'effectifs', clear=True)
        wks.update([df_report_effectifs.columns.values.tolist()] + df_report_effectifs.values.tolist())
