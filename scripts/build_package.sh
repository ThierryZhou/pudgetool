cd ..
python3 setup.py bdist_wheel
twine upload --repository pudgetool dist/* 
cd -
