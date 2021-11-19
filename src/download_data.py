# author : Hatef Rahmani
# date : 2021-11-19

""""Download data csv data from the web to the filepath as csv format"

Usage : src/download_data.py --url=<url> --out_file=<out_file>

options:
--url=<url>             URL to download the data (must standard csv format)
--out_file=<out_file>   Path to write the file locally
"""

from docopt import docopt
import pandas as pd
import os

opt = docopt(__doc__)

def main(url, out_file):

    data = pd.read_csv(url, header=None)
    try:
      data.to_csv(out_file, index = False)
    except:
      os.makedirs(os.path.dirname(out_file))
      data.to_csv(out_file, index = False)

if __name__ == "__main__":
  main(opt["--url"], opt["--out_file"])
