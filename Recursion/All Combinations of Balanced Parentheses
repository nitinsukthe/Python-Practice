def generateParentheses(n,Open,close,s,ans):
    if Open==n and close==n:
        ans.append(s)
        return
    if Open<n:
        generateParentheses(n,Open+1,close,s+"{",ans)
    if close<Open:
        generateParentheses(n,Open,close+1,s+"}",ans)
n=3
ans=[]
generateParentheses(n,0,0,"",ans)
for s in ans:
    print(s)
