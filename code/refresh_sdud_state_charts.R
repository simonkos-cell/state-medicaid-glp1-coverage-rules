################################################################################
# Purpose : Regenerate the per-state SDUD dispensing charts for weight-loss
#           GLP-1s (Wegovy, Saxenda, Zepbound), extended through the latest
#           available quarter. Produces, for every state, two charts in the
#           style of the originals:
#             <ST>.png      prescriptions by quarter (raw counts), by product
#             <ST>100K.png  prescriptions per 100,000 Medicaid enrollees by
#                           quarter, by product
#           These replace the 2024 Q4 versions in the state document folders
#           and should show the 1/1/2026 withdrawals (CA, NH, PA, SC) and the
#           other 2026 changes.
#
# Inputs  : (all relative to PROJECT_ROOT, set below)
#   raw_data/SDUD/raw_SDUD/  CMS SDUD annual CSVs, 2021 through 2026, as
#       listed by name in SDUD_FILES (the 2021-2024 files are the Dec 2025
#       updates; 2025 and 2026 are the July 2026 updates, running through
#       2026 Q1/Q2). clean_SDUD/ is empty, so raw CSVs are read directly.
#   raw_data/enrollment/pi-dataset-september-2026-release.csv
#       CMS Medicaid enrollment ("pi-dataset"), used for the per-100K rate.
#   NDC_LIST (public weight-loss NDC list; path set below)
#       Needs columns F3_ndc and Brand Name (the GLP1_Meds_FULL format).
#
# Outputs : OUT_DIR/quarterly_total_rx/<ST>.png
#           OUT_DIR/quarterly_rx_by_100K/<ST>100K.png
#           OUT_DIR/state_quarter_product_counts.csv
#           (OUT_DIR is set below; it points at ks_work/ because raw_data/ and
#           outputs/ in this project are not group writable for simonkos)
#             (the plotted numbers, so the charts are reproducible)
#
# Date    : 2026-11-15
# Author  : Kosali Simon
#
# Method  : Follows the original charting approach (Potter / Lande, 2025):
#           filter SDUD to the weight-loss GLP-1 NDCs by brand name, sum
#           number_rx by state x quarter x product, drop state "XX" and
#           product "UNKNOWN", join median quarterly enrollment (Final Report
#           == "Y") and compute number_rx / enrollment * 100000.
#
# Package versions assumed: R >= 4.2; data.table >= 1.14; dplyr >= 1.1;
#           ggplot2 >= 3.4; zoo >= 1.8; stringr >= 1.5; stringi >= 1.7;
#           haven >= 2.5 (only if USE_CLEAN_DTA). Install with
#           install.packages(c("data.table","dplyr","ggplot2","zoo","stringr",
#                              "stringi","haven")).
#
# Run on IU Quartz (verified 2026-11-15):
#   module load r/4.5.1
#   LD_PRELOAD=/N/soft/rhel8/gcc/14.2.0/lib64/libstdc++.so.6 \
#     R_DATATABLE_NUM_THREADS=4 Rscript ks_work/refresh_sdud_state_charts.R
#   The LD_PRELOAD is needed because the r/4.5.1 build resolves libstdc++ from
#   gcc/9.3.0 through a compiled-in RPATH. That copy lacks GLIBCXX_3.4.29, so
#   dplyr fails to load, and setting LD_LIBRARY_PATH does not help because
#   RPATH takes precedence over it. r/4.6.1 loads dplyr but has no zoo
#   installed, so 4.5.1 plus the preload is the working combination.
#   R_DATATABLE_NUM_THREADS caps data.table on the shared login node.
#
# Fails loudly: stops if an input file is missing, if the NDC filter matches
#           zero rows, or if any state-quarter has prescriptions but no
#           enrollment. Prints row counts after every merge and filter.
################################################################################

suppressPackageStartupMessages({
  library(data.table); library(dplyr); library(ggplot2); library(zoo)
  library(stringr);    library(stringi)
})
options(scipen = 9999)   # 10000 is out of range and R warns

# ------------------------------------------------------------------------------
# 0. Parameters. These are the only lines that normally need editing.
# ------------------------------------------------------------------------------
PROJECT_ROOT <- "/N/project/Simon_HealthEcProj1/medicaid_glp_short_letter"
# Raw CMS SDUD files, named as they sit in raw_data/SDUD/raw_SDUD/ (names are
# irregular across vintages, so they are listed explicitly rather than built
# from a pattern). Add a line when a new year or update arrives.
SDUD_FILES <- c(
  "2021" = "raw_data/SDUD/raw_SDUD/sdud-2021-updated-dec2025.csv",
  "2022" = "raw_data/SDUD/raw_SDUD/sdud-2022-updated-dec2025.csv",
  "2023" = "raw_data/SDUD/raw_SDUD/sdud-2023-updated-dec2025.csv",
  "2024" = "raw_data/SDUD/raw_SDUD/sdud-2024-updated-dec2025.csv",
  "2025" = "raw_data/SDUD/raw_SDUD/sdud2025_updatedjuly2026.csv",
  "2026" = "raw_data/SDUD/raw_SDUD/sdud2026_updated072026.csv"
)
YEARS        <- as.integer(names(SDUD_FILES))
USE_CLEAN_DTA <- FALSE               # clean_SDUD/ is empty; read raw CSVs
ENROLL_FILE  <- "raw_data/enrollment/pi-dataset-september-2026-release.csv"
# Public weight-loss NDC list. Keep this pointed at the public repo list, not
# at raw_data/ndc/, so the script is runnable by anyone on the project.
NDC_LIST     <- "ks_work/ndc_public/GLP1_Meds_FULL.csv"
WL_BRANDS    <- c("SAXENDA", "WEGOVY", "ZEPBOUND")
# Analysis universe: the 50 states plus DC. Territories are dropped because the
# CMS enrollment file has no denominator for them (Puerto Rico appears in SDUD
# from 2024 Q3 onward with no enrollment match). Dropped rows are printed.
STATES_KEEP  <- c(state.abb, "DC")
OUT_DIR      <- "ks_work/outputs/figures/state_profiles"

setwd(PROJECT_ROOT)
dir.create(file.path(OUT_DIR, "quarterly_total_rx"),  recursive = TRUE, showWarnings = FALSE)
dir.create(file.path(OUT_DIR, "quarterly_rx_by_100K"), recursive = TRUE, showWarnings = FALSE)

must_exist <- function(p) if (!file.exists(p)) stop("Missing input: ", p)

# ------------------------------------------------------------------------------
# 1. Weight-loss GLP-1 NDC list
# ------------------------------------------------------------------------------
must_exist(NDC_LIST)
ndc <- fread(NDC_LIST, colClasses = "character")
if (!all(c("F3_ndc", "Brand Name") %in% names(ndc)))
  stop("NDC list needs columns F3_ndc and 'Brand Name'")
ndc[, F3_ndc := stri_pad_left(F3_ndc, 11, pad = "0")]
ndc[, brand   := toupper(word(`Brand Name`, 1))]
wl_ndc <- unique(ndc[brand %in% WL_BRANDS, F3_ndc])
cat("Weight-loss NDCs in list:", length(wl_ndc), "\n")
if (length(wl_ndc) == 0) stop("No weight-loss NDCs matched brands ", paste(WL_BRANDS, collapse = ", "))

# ------------------------------------------------------------------------------
# 2. SDUD, all years, filtered to those NDCs
# ------------------------------------------------------------------------------
read_sdud_year <- function(yr) {
  if (USE_CLEAN_DTA) {
    f <- sprintf("raw_data/SDUD/clean_SDUD/sdud_%d.dta", yr); must_exist(f)
    d <- as.data.table(haven::read_dta(f))
    setnames(d, old = c("state","ndc","product_name","year","quarter","number_rx"),
                new = c("state","ndc","product_name","year","quarter","number_rx"),
                skip_absent = TRUE)
  } else {
    f <- SDUD_FILES[[as.character(yr)]]; must_exist(f)
    d <- fread(f, colClasses = "character")   # read all as text; cast below
    # CMS column names vary by vintage ("Number of Prescriptions",
    # "numberofprescriptions", "number_rx"). Normalize by stripping everything
    # except letters and lower-casing, then match.
    nm   <- names(d)
    norm <- tolower(gsub("[^A-Za-z]", "", nm))
    pick <- function(cands) {
      h <- nm[norm %in% cands]
      if (!length(h)) stop(sprintf("In %s, no column matched any of: %s. Columns present: %s",
                                   f, paste(cands, collapse = "/"), paste(nm, collapse = ", ")))
      h[1]
    }
    d <- d[, .(state        = get(pick(c("state"))),
               ndc          = get(pick(c("ndc"))),
               product_name = get(pick(c("productname"))),
               year         = as.integer(get(pick(c("year")))),
               quarter      = as.integer(get(pick(c("quarter")))),
               number_rx    = as.numeric(get(pick(c("numberofprescriptions","numberrx")))))]
  }
  d[, ndc := stri_pad_left(as.character(ndc), 11, pad = "0")]
  n0 <- nrow(d)
  d  <- d[ndc %in% wl_ndc]
  cat(sprintf("SDUD %d: %s rows read, %s rows for weight-loss NDCs\n", yr, format(n0, big.mark=","), format(nrow(d), big.mark=",")))
  d
}
sdud <- rbindlist(lapply(YEARS, read_sdud_year), use.names = TRUE)
if (nrow(sdud) == 0) stop("SDUD filter returned zero rows")

sdud[, product_name := toupper(sub(" .*$", "", product_name))]
sdud <- sdud[!str_detect(product_name, "UNKNOWN") & state != "XX"]
n_pre   <- nrow(sdud)
dropped <- sdud[!state %in% STATES_KEEP,
                .(rows = .N, number_rx = sum(number_rx, na.rm = TRUE)), by = state]
if (nrow(dropped)) { cat("Jurisdictions dropped (no enrollment denominator):\n"); print(dropped) }
sdud <- sdud[state %in% STATES_KEEP]
cat(sprintf("Rows before state filter: %s; after: %s\n",
            format(n_pre, big.mark = ","), format(nrow(sdud), big.mark = ",")))
sdud[, yr_qrt := as.yearqtr(paste(year, quarter, sep = " Q"))]

counts <- sdud[, .(number_rx = sum(number_rx, na.rm = TRUE)), by = .(state, yr_qrt, product_name)]
cat("State x quarter x product rows:", nrow(counts), "\n")

# ------------------------------------------------------------------------------
# 3. Enrollment (median monthly Total Medicaid Enrollment within quarter)
# ------------------------------------------------------------------------------
must_exist(ENROLL_FILE)
enr <- fread(ENROLL_FILE)
need <- c("State Abbreviation", "Reporting Period", "Total Medicaid Enrollment", "Final Report")
if (!all(need %in% names(enr))) stop("Enrollment file missing one of: ", paste(need, collapse = ", "))
enr <- enr[`Final Report` == "Y",
           .(state  = `State Abbreviation`,
             yr_qrt = as.yearqtr(as.Date(paste0(substr(as.character(`Reporting Period`),1,4), "-",
                                                 substr(as.character(`Reporting Period`),5,6), "-01"))),
             enrollment = as.numeric(`Total Medicaid Enrollment`))]
enr <- enr[, .(enrollment = median(enrollment, na.rm = TRUE)), by = .(state, yr_qrt)]
cat("Enrollment state x quarter rows:", nrow(enr), "\n")

# ------------------------------------------------------------------------------
# 4. Merge and rate
# ------------------------------------------------------------------------------
n_before <- nrow(counts)
merged <- merge(counts, enr, by = c("state", "yr_qrt"), all.x = TRUE)
stopifnot(nrow(merged) == n_before)
unmatched <- merged[is.na(enrollment)]
cat(sprintf("Merged rows: %d; rows with no enrollment match: %d (%.1f%%)\n",
            nrow(merged), nrow(unmatched), 100 * nrow(unmatched) / nrow(merged)))
if (nrow(unmatched) > 0) {
  print(unique(unmatched[, .(state, yr_qrt)]))
  stop("Some state-quarters have prescriptions but no enrollment; fix the enrollment file or YEARS before plotting.")
}
merged[, number_rx_100K := number_rx / enrollment * 100000]

# Write the plotted numbers with readable year and quarter columns. yr_qrt is
# an as.yearqtr object, which fwrite would otherwise store as a decimal
# (2022.25 for 2022 Q2); the deposited file should be readable without knowing
# that convention.
out_counts <- copy(merged)[order(state, yr_qrt, product_name)]
out_counts[, `:=`(year         = as.integer(format(yr_qrt, "%Y")),
                  quarter      = as.integer(substr(format(yr_qrt, "%q"), 1, 1)),
                  year_quarter = format(yr_qrt, "%Y Q%q"))]
out_counts[, yr_qrt := NULL]
setcolorder(out_counts, c("state", "year", "quarter", "year_quarter",
                          "product_name", "number_rx", "enrollment",
                          "number_rx_100K"))
fwrite(out_counts, file.path(OUT_DIR, "state_quarter_product_counts.csv"))

# ------------------------------------------------------------------------------
# 5. Charts, one pair per state
# ------------------------------------------------------------------------------
states <- sort(unique(merged$state))
cat("Plotting", length(states), "states\n")
for (st in states) {
  df <- merged[state == st][order(yr_qrt)]
  df[, yr_qrt_f := factor(format(yr_qrt, "%Y Q%q"), levels = unique(format(yr_qrt, "%Y Q%q")))]

  p1 <- ggplot(df, aes(yr_qrt_f, number_rx, colour = product_name, group = product_name)) +
    geom_line(linewidth = 1) + geom_point(size = 2) +
    labs(title = paste0("prescriptions in ", st), x = "yr_qrt", y = "number_rx") +
    theme(plot.title = element_text(hjust = 0.5, size = 14),
          axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "right")
  ggsave(file.path(OUT_DIR, "quarterly_total_rx", paste0(st, ".png")), p1, width = 9, height = 5.5, dpi = 200)

  p2 <- ggplot(df, aes(yr_qrt_f, number_rx_100K, colour = product_name, group = product_name)) +
    geom_line(linewidth = 1) + geom_point(size = 2) +
    labs(title = paste0("GLP1 prescriptions for 100,000 enrollees in ", st), x = "yr_qrt", y = "number_rx_100K") +
    theme(plot.title = element_text(hjust = 0.5, size = 14),
          axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "right")
  ggsave(file.path(OUT_DIR, "quarterly_rx_by_100K", paste0(st, "100K.png")), p2, width = 9, height = 5.5, dpi = 200)
}
cat("Done. Charts in", file.path(PROJECT_ROOT, OUT_DIR), "\n")
