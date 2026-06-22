class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogcolor = image[sr][sc]
        visited = set()
        
        def ff(sr,sc):
            ROW,COL = len(image) , len(image[0])
            if sr >= ROW or sc >=COL or min(sr,sc)<0 or (sr,sc) in visited or image[sr][sc]!=ogcolor:
                return
            
            image[sr][sc]=color
            visited.add((sr,sc))
            ff(sr+1,sc)
            ff(sr,sc+1)
            ff(sr,sc-1)
            ff(sr-1,sc)
            
        ff(sr,sc)
        
        return image
            