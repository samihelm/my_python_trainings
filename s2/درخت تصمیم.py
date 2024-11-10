patron = input('patron?')
if patron == 'full':
    w_e = float(input('w_e? '))
    if w_e > 60:
        print('no')
    elif 30<w_e<=60:
        alternate = input('alternate? ')
        if alternate == 'no':
            reservation = input('reservation? ')
            if reservation == 'no':
                bar = input('bar? ')
                if bar == 'no':
                    print('no')
                elif bar == 'yes':
                    print('yes')
                else:
                    print('not defiend')
            elif reservation == 'yes':
                print('yes')
            else:
                print('not defiend')
        elif alternate == 'yes':
            fri_sat = input('fri_sat? ')
            if fri_sat == 'no':
                print('no')
            elif fri_sat =='yes':
                print('yes')
            else:
                print('not defiend')
            
        else:
            print('not defiend')
    elif 10<w_e<=30:
       hungry = input('hungry? ')
       if hungry == 'no':
           print('yes')
       elif hungry == 'yes':
           alternate = input('alternate? ')
           if alternate == 'no':
               print('yes')
           elif alternate == 'yes':
               raining = input('raining? ')
               if raining == 'no':
                   print('no')
               elif raining == 'yes':
                   print('yes')
               else:
                   print('not defiend')
           
    elif 0<w_e<=10:
        print('yes')
    else:
        print('not defiend')
elif patron == 'some':
    print('yes')
elif patron == 'none':
    print('no')
else:
    print('not defiend')
