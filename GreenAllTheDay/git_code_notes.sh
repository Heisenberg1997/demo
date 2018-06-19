echo "start git add commit fetch merge push"
echo "git add -A"
DATE=`date +"%Y-%m-%d"`
cd ~/11
git add -A

echo "git commit -m 'leetcode-louyuting'"
git commit -m DATE

echo "git fetch origin master"

echo "git merge origin/master"

echo "git push origin master:master"
git push origin HEAD
