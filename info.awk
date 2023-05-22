#!/usr/bin/awk -f
# usage: mark dept header from dept list on match dept::keyword
# marke ref to para ie. para 2.2.1

@include "min_lib.awk"
BEGIN { IGNORECASE=1 }
{ rep_with(); print }
