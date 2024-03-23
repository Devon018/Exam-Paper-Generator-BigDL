# exam-zh 项目
# 复制文件到 release 目录

# 仓库路径
originpath="/Users/xiakangwei/Nutstore/Github/repository/exam-zh"
origindoc="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/doc"
# release 目录路径
targetpath="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/release"


for i in CHANGELOG.md README.md LICENSE example-single.tex example-single.pdf example-multiple.tex example-multiple.pdf ; do
  cp -r "$originpath"/$i "$targetpath"/$i
done

cp -r "$originpath"/*.sty "$targetpath"/
cp -r "$originpath"/exam-zh.cls "$targetpath"/
cp -r "$origindoc"/exam-zh-doc.pdf "$targetpath"/

# 去掉原来的 zip 文件
rm "$targetpath"/*.zip

# 复制 "exam-zh-v.zip" 到剪切板
echo "exam-zh-v" | pbcopy

open "$targetpath"/

# 打开 YemuZip 程序进行压缩
open -a YemuZip.app "$targetpath"/*