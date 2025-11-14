# Tesi-metriche-extractor.py
import pandas as pd
import numpy as np
# To analyse a file, replace the file path with the path of the file you want to analyse.
FILE_PATH = "C:/Users/Utente/Desktop/replication_package/ReplicationPackage_Messa/SC/ref4 CD/Understand-sc-ref4.xlsx"
COLUMN  = ["CountLineCode", "AvgCyclomatic", "CountDeclMethod", "MaxCyclomatic", "CountClassCoupled", "PercentLackOfCohesion"]

def main():
    df = pd.read_excel(FILE_PATH)
    dga = pd.DataFrame()
    squinzi = pd.DataFrame()
    if "Kind" in df.columns:
        keep = df["Kind"].str.contains("Class|Interface|Enum|Annotation", case=False, na=False)
        anon = df["Kind"].str.contains("Anonymous|Function|Method|Unknown", case=False, na=False)
        squinzi = df[keep & ~anon].copy()
        is_file = df["Kind"].str.contains("File", case=False, na=False)
        is_class = df["Name"].str.contains(r"\.java$", case=False, na=False)
        dga = df[is_file & is_class].copy()
    file(dga)
    classe(squinzi)
    pkg_overall(squinzi)

def file(df):
    print("\n=== FILES level metrics ===")
    # LOC
    locSum = pd.to_numeric(df[COLUMN[0]], errors="coerce").sum()
    print(f"'{COLUMN[0]}' = {locSum}")

    # AvgCyclomatic
    avgCyclo = pd.to_numeric(df[COLUMN[1]], errors="coerce").mean()
    print(f"'AvgCyclomatic' = {avgCyclo}")

    # MaxCyclomatic
    s = pd.to_numeric(df[COLUMN[3]], errors="coerce").max()
    print(f"'{COLUMN[3]}' = {s}")

def classe(df):
    print("\n=== CLASSES level metrics ===")
    #CountClassCoupled avg
    s = pd.to_numeric(df[COLUMN[4]], errors="coerce").mean()
    print(f"'{COLUMN[4]}' (avg) = {s}")

    # CountClassCoupled median
    s = pd.to_numeric(df[COLUMN[4]], errors="coerce").median()
    print(f"'{COLUMN[4]}' (median) = {s}")

    # CountClassCoupled p90
    s = pd.to_numeric(df[COLUMN[4]], errors="coerce").quantile(0.9)
    print(f"'{COLUMN[4]}' (p90) = {s}")

    # PercentLackOfCohesion Avg W
    a = pd.to_numeric(df[COLUMN[5]], errors="coerce")
    b = pd.to_numeric(df[COLUMN[2]], errors="coerce")
    num =   (a * b).sum(skipna=True)
    den = b.sum()
    print(f"'{COLUMN[5]}' (Avg W) = {num/den}")

    # PercentLackOfCohesion median
    s = pd.to_numeric(df[COLUMN[5]], errors="coerce").replace(0, pd.NA).dropna().median()
    print(f"'{COLUMN[5]}' (median) = {s}")

    # PercentLackOfCohesion p90
    s = pd.to_numeric(df[COLUMN[5]], errors="coerce").replace(0, pd.NA).dropna().quantile(0.9)
    print(f"'{COLUMN[5]}' (p90) = {s}")

# =========================
#       FOR PACKAGE
# =========================

def pkg_overall(df):

    # obtains the package from the qualified name
    df["Package"] = df["Name"].apply(lambda s: s.rsplit(".", 1)[0] if isinstance(s, str) and "." in s else "")

    df["CBO"]   = pd.to_numeric(df[COLUMN[4]], errors="coerce")  # CountClassCoupled
    df["LCOM"]  = pd.to_numeric(df[COLUMN[5]], errors="coerce")  # PercentLackOfCohesion
    df["METH"]  = pd.to_numeric(df[COLUMN[2]], errors="coerce")  # CountDeclMethod

    g = df.groupby("Package", dropna=False)

    # --- PACKAGE Stats ---
    per_pkg = pd.DataFrame({
        "Classes": g.size(),
        "AvgCoupled":    g["CBO"].mean(),
        "MedianCoupled": g["CBO"].median(),
        "P90Coupled":    g["CBO"].quantile(0.90),
    })

    # LCOM% for-package
    # Weighted average in the package: sum(LCOM * METH) / sum(METH)
    weighted_sum = (df["LCOM"] * df["METH"]).groupby(df["Package"], dropna=False).sum(min_count=1)
    weights      = df["METH"].groupby(df["Package"], dropna=False).sum(min_count=1).replace(0, np.nan)
    per_pkg["AvgLCOM_W"]   = (weighted_sum / weights)

    # median e P90 for-package (0 ignored)
    lcom_nz = df["LCOM"].replace(0, np.nan)
    per_pkg["MedianLCOM"]  = lcom_nz.groupby(df["Package"], dropna=False).median()
    per_pkg["P90LCOM"]     = lcom_nz.groupby(df["Package"], dropna=False).quantile(0.90)

    # --- single numbers ‘among the packages’ (each package weighs the same) ---
    cbo_avg_all_pkgs    = per_pkg["AvgCoupled"].mean(skipna=True)
    cbo_median_all_pkgs = per_pkg["MedianCoupled"].median(skipna=True)
    cbo_p90_all_pkgs    = per_pkg["AvgCoupled"].quantile(0.90, interpolation="linear")

    lcom_median_all_pkgs = per_pkg["MedianLCOM"].median(skipna=True)
    lcom_p90_all_pkgs    = per_pkg["AvgLCOM_W"].quantile(0.90, interpolation="linear")
    lcom_wavg_all_pkgs   = per_pkg["AvgLCOM_W"].mean(skipna=True)

    print("\n=== Summary OF THE PACKAGES ===")
    print(f"CountClassCoupled (AVG)    = {cbo_avg_all_pkgs}")
    print(f"PercentLackOfCohesion (W AVG)  = {lcom_wavg_all_pkgs}")
if __name__ == "__main__":
    main()
