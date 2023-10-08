<?php
function main(){
  echo("Hello, World!!!\n");
};

if (!count(debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS))) {
  main();
};