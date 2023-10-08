sub main {
  print "Hello, World!!!\n";
}

unless (caller) {
  main;
}