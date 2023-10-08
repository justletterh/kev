function main()
    print("Hello, World!!!")
  end
  
  if not pcall(debug.getlocal, 4, 1) then
    main()
  end