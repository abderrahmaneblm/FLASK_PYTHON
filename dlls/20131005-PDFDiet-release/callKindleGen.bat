@echo off
rem %1 == テンポラリフォルダに出力される .opf ファイルのパス
rem %2 == テンポラリフォルダに出力する mobi ファイル名(パスなしのファイル名だけ)
rem %3 == テンポラリフォルダに出力する mobi ファイルのパス(フルパス)
rem %4 == 最終出力フォルダのパス(ファイル名付き)

rem kindlegen.exe %1 -verbose -c2 -unicode -o %3
kindlegen.exe %1 -verbose -c2 -o %2
kindlestrip.exe %3 %4
rem pause
