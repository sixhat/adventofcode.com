#/bin/sh    
set -e
# figlet -c ADVENT OF CODE 2023
cat << EOF
    _    ______     _______ _   _ _____    ___  _____    ____ ___  ____  _____ 
   / \  |  _ \ \   / / ____| \ | |_   _|  / _ \|  ___|  / ___/ _ \|  _ \| ____|
  / _ \ | | | \ \ / /|  _| |  \| | | |   | | | | |_    | |  | | | | | | |  _|  
 / ___ \| |_| |\ V / | |___| |\  | | |   | |_| |  _|   | |__| |_| | |_| | |___ 
/_/   \_\____/  \_/  |_____|_| \_| |_|    \___/|_|      \____\___/|____/|_____|
                                                                               
                             ____   ___ ____  _____ 
                            |___ \ / _ \___ \|___ / 
                              __) | | | |__) | |_ \ 
                             / __/| |_| / __/ ___) |
                            |_____|\___/_____|____/ 
EOF


echo
echo == Problema 1 ==
python3 01/p01.py

echo
echo == Problema 2 ==
python3 02/p02.py

echo
echo ==Problema 3 ==
python3 03/p03.py

echo
echo ==Problema 4 ==
python3 04/p04.py

echo
echo ==Problema 5
cd 05 || exit 
python3 p05.py
cd ..

echo
echo ==Problema 6 ==
python3 06/p06.py

echo
echo ==Problema 7 ==
python3 07/p07.py

echo
echo ==Problema 8 ==
python3 08/p08.py

echo
echo ==Problema 9 ==
cd 09 || exit
python3 p09.py 
cd ..

echo
echo ==Problema 10 ==
cd 10 || exit
python3 p10.py 
cd ..

echo
echo ==Problema 11 ==
cd 11 || exit
python3 p11.py 
cd ..



