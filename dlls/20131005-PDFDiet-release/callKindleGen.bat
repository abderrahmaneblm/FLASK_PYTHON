@echo off
rem %1 == �e���|�����t�H���_�ɏo�͂���� .opf �t�@�C���̃p�X
rem %2 == �e���|�����t�H���_�ɏo�͂��� mobi �t�@�C����(�p�X�Ȃ��̃t�@�C��������)
rem %3 == �e���|�����t�H���_�ɏo�͂��� mobi �t�@�C���̃p�X(�t���p�X)
rem %4 == �ŏI�o�̓t�H���_�̃p�X(�t�@�C�����t��)

rem kindlegen.exe %1 -verbose -c2 -unicode -o %3
kindlegen.exe %1 -verbose -c2 -o %2
kindlestrip.exe %3 %4
rem pause
