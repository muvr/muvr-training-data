#!/usr/bin/awk -f
FILEN==0{
  CMD="mkdir -p " out "/training 2>/dev/null"
  system(CMD)
  close(CMD)
  CMD="mkdir -p " out "/test 2>/dev/null"
  system(CMD)
  close(CMD)
  TRAIN_DIR=out "/training"
  TEST_DIR=out "/test"
  print "Training directory: " TRAIN_DIR
  print " Testing directory: " TEST_DIR
  print "     Testing ratio: " (ratio * 100) "%"
}
FNR==1 {
  FILEN=FILEN+1
  if (o) close(o);
  FILE=FILENAME;sub(".*/", "", FILE)
  if (ratio == 0) DIR=TRAIN_DIR
  else if (FILEN % int(1/ratio) == 0) DIR=TEST_DIR
  else DIR=TRAIN_DIR
  o=DIR "/" FILE
  print FILE " -> " DIR
}
BEGIN { FS=","; OFS="," }
mode=="slacking"{
  if ( $4 == "" ) $4 = "-"
  else $4 = "E"
  print > o
}
mode!="slacking"{
  if ( $4 != "" ) {
    gsub(/ /, "", $4)
    $4 = tolower($4)
    if ($4 == "bc") { $4 = "arms/bicep-curl" }
    else if ($4 == "te") { $4 = "arms/tricep-extension" }
    else if ($4 == "tc") { $4 = "arms/tricep-extension" }
    else if ($4 == "lr") { $4 = "arms/lateral-raise" }
    else if ($4 == "bicep") { $4 = "arms/bicep-curl" }
    else if ($4 == "tricep") { $4 = "arms/tricep-extension" }
    else if ($4 == "lateral") { $4 = "arms/lateral-raise" }
    print > o
  }
}
