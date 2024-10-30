import pandas as pd
import argparse
import os
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def gff_to_xlsx(gff_file, output_xlsx):
    try:
        if not os.path.isfile(gff_file):
            logging.error(f"The file '{gff_file}' does not exist.")
            return

        logging.info("Reading GFF file...")
        gff_df = pd.read_csv(gff_file, sep='\t', comment='#', header=None,
                             names=['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])

        logging.info("Processing attributes...")
        attributes = gff_df['attributes'].str.split(';').apply(lambda x: dict(item.split('=') for item in x if '=' in item))
        attributes_expanded_df = attributes.apply(pd.Series)

        logging.info("Combining data...")
        gff_expanded_df = pd.concat([gff_df.drop(columns=['attributes']), attributes_expanded_df], axis=1)

        logging.info(f"Writing to '{output_xlsx}'...")
        gff_expanded_df.to_excel(output_xlsx, index=False)
        logging.info(f"Success: GFF file converted to '{output_xlsx}'.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Convert a GFF file to an Excel (XLSX) file.")
    parser.add_argument("gff_file", help="Path to the GFF file.")
    parser.add_argument("output_xlsx", help="Path to save the output XLSX file.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity.")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    gff_to_xlsx(args.gff_file, args.output_xlsx)

if __name__ == "__main__":
    main()
