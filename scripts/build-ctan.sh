# exam-zh 项目
# 复制文件到 CTAN 目录

# 仓库路径
originpath="/Users/xiakangwei/Nutstore/Github/repository/exam-zh"
origindoc="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/doc"
# CTAN 目录路径
targetpath="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/CTAN/exam-zh"
targetdoc="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/CTAN/exam-zh/doc"
targettex="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/CTAN/exam-zh/tex"
targetexamples="/Users/xiakangwei/Nutstore/Github/repository/exam-zh/CTAN/exam-zh/examples"


# 到 CTAN/exam-zh/ 的文件
for i in CHANGELOG.md README.md LICENSE ; do
  cp -r "$originpath"/$i "$targetpath"/$i
done

# 到 CTAN/exam-zh/tex/ 的文件
cp -r "$originpath"/*.sty "$targettex/"
cp -r "$originpath"/*.cls "$targettex/"

# 到 CTAN/exam-zh/doc/ 的文件
for i in xdyydoc.cls exam-zh-doc-setup.tex exam-zh-doc.tex exam-zh-doc.pdf ; do 
  cp -r "$origindoc"/$i "$targetdoc"/$i
done

cp -r "$origindoc"/back/*.tex "$targetdoc"/back/
cp -r "$origindoc"/body/*.tex "$targetdoc"/body/
cp -r "$origindoc"/figures/* "$targetdoc"/figures/

# 到 CTAN/exam-zh/examples/ 的文件
for i in example-single.tex example-single.pdf example-multiple.tex example-multiple.pdf ; do
  cp -r "$originpath"/$i "$targetexamples"/$i
done

echo "exam-zh.zip" | pbcopy

# 去掉旧的 zip 文件
rm "$targetpath"/../*.zip

# 打开目录
open "$targetpath"/../

# 打开 YemuZip 程序进行压缩
open -a YemuZip.app "$targetpath"/../exam-zh