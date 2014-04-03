#-*- coding: utf-8 -*-
from Board import Board
import sys, os

def clear_console():
    os.system(['clear','cls'][os.name == 'nt'])

def game_loop():
    clear_console();
    try: boyut = int(raw_input("Tahta boyutu: "));
    except ValueError: boyut = 3;
    board = Board(boyut)
    clear_console();
    print "Oyun başladı!";
    print "Lütfen işaretlemek istediğiniz Satır/Sütun(Örnek: Satır 1, Sütun 1) belirterek giriniz."
    print "İlk hamle X'e ait."
    board.print_table();

    while board.not_over():
        try:
            row = int(raw_input("Satır: "))
            column = int(raw_input("Sütun: "))
        except ValueError:
            print "Lütfen bir sayı giriniz."
            continue
        if row > board.size or column > board.size: print "Lütfen sınırlar içinde bir sayı giriniz. Satır, Sütun: ("+ str(board.size) +","+ str(board.size) +")"; continue

        clear_console();
        if not board.play(row - 1, column - 1):
            print "Geçersiz işaretleme. Tekrar deneyiniz."

        print "Şuan sıra: " + ("X" if board.turn == 0 else "O")
        board.print_table()

    print "Oyun bitti! " + ("Sonuç: Berabere." if board.winner == -1 else "Kazanan:" + ("X" if board.winner == 0 else "O"))
    answer = raw_input("Yeniden başlamak için R, oyunu kapatmak için başka herhangi bir karakter giriniz: ")
    game_loop() if answer.strip().lower() == 'r' else sys.exit(0);

game_loop();