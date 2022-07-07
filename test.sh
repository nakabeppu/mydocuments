make clean
make html
rm -r ./docs
mkdir ./docs
cp -rp _build/html/* ./docs
cd ./docs
touch .nojekyll
# git add .
# git status
# git commit -m "shellによるプッシュ"
# git status
cd ../
open _build/html/index.html
