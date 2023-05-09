import pandas as pd


if __name__ == '__main__':
    df_techniques = pd.read_excel(r".\excel_sheets\Techniques_options.xlsx")
    df_tactics = pd.read_excel(r".\excel_sheets\Tactics_options.xlsx")
    df_dpc_export = pd.read_excel(r".\excel_sheets\dpc_techniques_export.xlsx")

    technique_dict = dict(zip(df_techniques.Code, df_techniques.Name))
    tactics_list = list(df_tactics.Name)
    new_tactics = []
    new_techniques = []

    for tac in list(df_dpc_export.Tactics):
        new_tac = []
        for item in tactics_list:
            if item.replace(" ", "").lower() in f"{tac}".lower():
                new_tac.append(item)
        new_tactics.append(';'.join(new_tac))

    for tec in list(df_dpc_export.Techniques):
        new_tec = []
        for key, val in technique_dict.items():
            if key in f"{tec}":
                new_tec.append(val)
        new_techniques.append(';'.join(new_tec))

    df_dpc_export['New Tactics'] = new_tactics
    df_dpc_export['New Techniques'] = new_techniques
    df_dpc_export.to_excel(r".\excel_sheets\dpc_techniques_import.xlsx")

    print("Task complete.")
