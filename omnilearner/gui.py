import sys
from pathlib import Path
from streamlit import cli as stcli

def run():
    file_path = Path(__file__).resolve().parent / 'omni_learner.py'
    ST_PATH = Path.home() / ".streamlit"

    for folder in [ST_PATH]:
        if not folder.is_dir():
            folder.mkdir()

    #Check if streamlit credentials exists
    ST_CREDENTIALS = ST_PATH / 'credentials.toml'
    if not ST_CREDENTIALS.is_file():
        with ST_CREDENTIALS.open('w') as file:
            file.write("[general]\n")
            file.write('\nemail = ""')

    print(f'Starting Omnilearner from {file_path}')

    args = ["streamlit", "run", str(file_path), "--global.developmentMode=false", "--browser.gatherUsageStats=False"]

    sys.argv = args

    sys.exit(stcli.main())
