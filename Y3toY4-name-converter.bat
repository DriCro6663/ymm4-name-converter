@rem 文字コード Shift-JIS -> UTF-8 変更
chcp 65001

@rem 参照するファイルを更新
cd ./dist/Y3toY4-name-converter
rmdir "./01-新きつね"
rmdir "./02-QH"
rmdir "./03-Other"
rmdir "./10-result"
mkdir "./01-新きつね"
mkdir "./02-QH"
mkdir "./03-Other"
mkdir "./10-result"
cd ../..
xcopy /e "./01-新きつね" "./dist/Y3toY4-name-converter/01-新きつね"
xcopy /e "./02-QH" "./dist/Y3toY4-name-converter/02-QH"
xcopy /e "./03-Other" "./dist/Y3toY4-name-converter/03-Other"

@rem Touhou-LW-Farm-Quest-RPA.exe 起動
cd ./dist/Y3toY4-name-converter
Y3toY4-name-converter.exe

@rem 参照するファイルを更新
cd ../..
xcopy /e "./dist/Y3toY4-name-converter/10-result" "./10-result"

echo 終了するには何かキーを押してください...
pause > nul
exit