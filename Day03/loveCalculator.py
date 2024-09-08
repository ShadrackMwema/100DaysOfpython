print('''       _,--._.-,                        _,--._.-,             
      /\_r-,\_ )                       /\_r-,\_ )             
   .-.) _;='_/ (.;                  .-.) _;='_/ (.;           
    \ \'     \/S )                   \ \'     \/S )           
     L.'-. _.'|-'                     L.'-. _.'|-'            
    <_`-'\'_.'/                      <_`-'\'_.'/              
      `'-._( \                         `'-._( \               
             \\       ___               ___   \\,      ___    
              \\   .-'_. /              \ .'-. \\   .-'_. /   
               \\ /.-'_.'                '._' '.\\/.-'_.'     
                \('--'	                    '--``\('--'       
           snd    \                         snd   \\          
                                                  `\\,        
                                     diddled by jgs \|       ''')
name1 = input("Enter your name: ").lower()
name2 = input("Enter second name ").lower()

combined = name1 + name2
print(combined)

t_count = combined.count("t")
r_count = combined.count("r")
u_count = combined.count("u")
e_count = combined.count("e")

true_count = t_count + r_count + u_count + e_count

l_count = combined.count("l")
o_count = combined.count("o")
v_count = combined.count("v")
e_count = combined.count("e")

love_count = l_count + o_count + v_count+e_count

love = str(true_count)+str(love_count)
love = int(love)

if love<10 or love >90:
    print(f"Your love is {love} you go to together")
elif love>=40 or love <=50:
    print(f"Your love is {love} you go to together")