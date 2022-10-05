import requests
import argparse
banner = """

@@@@@@@        @@@   @@@@@@@   @@@  @@@     @@@  @@@   @@@@@@@@   @@@@@@@    @@@@@@   @@@@@@   
@@@@@@@@      @@@@   @@@@@@@@  @@@  @@@     @@@  @@@  @@@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@  
@@!  @@@     @@!@!   @@!  @@@  @@!  !@@     @@!  @@@  @@!   @@@@  @@!  @@@  !@@           @@@  
!@!  @!@    !@!!@!   !@!  @!@  !@!  @!!     !@!  @!@  !@!  @!@!@  !@!  @!@  !@!           @!@  
@!@  !@!   @!! @!!   @!@!!@!   @!@@!@!      @!@!@!@!  @!@ @! !@!  @!@!!@!   !!@@!!    @!@!!@   
!@!  !!!  !!!  !@!   !!@!@!    !!@!!!       !!!@!!!!  !@!!!  !!!  !!@!@!     !!@!!!   !!@!@!   
!!:  !!!  :!!:!:!!:  !!: :!!   !!: :!!      !!:  !!!  !!:!   !!!  !!: :!!        !:!      !!:  
:!:  !:!  !:::!!:::  :!:  !:!  :!:  !:!     :!:  !:!  :!:    !:!  :!:  !:!      !:!       :!:  
 :::: ::       :::   ::   :::   ::  :::     ::   :::  ::::::: ::  ::   :::  :::: ::   :: ::::  
:: :  :        :::    :   : :   :   :::      :   : :   : : :  :    :   : :  :: : :     : : :   
                                                                                                                             
	#  Author: Dhaval Ramani (@d4rkh0rse)
	#  URL: https://github.com/d4rkh0rse/upi_osint
"""

if __name__ == '__main__':
    print(banner)
    
    target = input('Enter phone number or UPI ID: ')
    main_url = 'https://upibankvalidator.com/api/upiValidation?upi='
    upi_ids = ['apl','oksbi','okhdfcbank','sbi','okicici','axisbank','ikwik','pnb','hdfc','idfcbank','okaxis','abfspay','ybl','barodapay','upi','paytm','yapl']

    if len(target) > 9:

        if target.find('@')!=-1:
            response = requests.post(main_url+target).json()

            if response['isUpiRegistered']:
                # print('found')
                print(f"UPI Holder Name: {response['name']}",f"| UPI platform: {target.partition('@')[2]}")
            else:
                print('Invalid UPI ID.')
        else:
            for i in upi_ids:
                response = requests.post(main_url+target+'@'+i).json()
                if response['isUpiRegistered']:
                    # print('found')
                    print(f"UPI Holder Name: {response['name']}",f"| UPI platform: {i}")
                else:
                    print('Invalid UPI ID.')
    else:
        print('Enter Correct UPI ID or Phone Number')