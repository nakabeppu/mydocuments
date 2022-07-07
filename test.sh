make clean
make html
mkdir -p ./docs
rm -r ./docs/*
cp -rp _build/html/* ./docs
# git add .
# git status
# git commit -m "shellによるプッシュ"
# git status
open _build/html/index.html
