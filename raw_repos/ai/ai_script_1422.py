def find_duplicates(spreadsheet):
    df = pd.read_excel(spreadsheet)
    return df['A'][df['A'].duplicated(keep=False)]