# git 使用笔记

    - 比较两分支文件不同
    - git diff branch_1 branch_2 --stat
    - 比较两分支相同文件修改
    - git diff branch_1 branch_2 matching/settings.py

    - pr 之前如果不能自动合并，合并分支
    - git merge source target

## 删除本地分支并重新拉取远程分支
    需要切换到其他分支
    然后删除本地分支
    拉取远程分支
    - git fetch origin temp:temp

## rebase 使用
    如果多次合并提交，可以使用rebase 来进行变基 然后对分支进行合并
    -- git rebase -i <hard>
    -- 在 vim 中选择需要 保留的 commit
    -- 删除未注释的commit内容，然后填写合并后需要提交的内容
    -- git pull --rebase <source> <branch>
    
    -- git rebase <source> 可以使用source分支为基分支 此分支需要切换一下分支，否则该分支仍然不是最新代码
    
    当rebase中修改重复时，代码时在一个临时分支，添加过修改后到文件后无需commit 直接 continue即可
## 修改前一次提交
    如果只想一次提交内容，那么使用 amend 参数来修改上次提交，此时只提交一次commit
    -- git commit --amend 
    -- git commit --amend -m "new message"
    -- git commit  --amend --author=xxx 修改提交用户
    -- git pull origin master:master 从远程

## 提交到远程分支
    -- git push <origin>:<branch> -[f]
    -- git push
## 注意
	rebase过程中，由于修改了commit的顺序，所以需要强推 才可以
