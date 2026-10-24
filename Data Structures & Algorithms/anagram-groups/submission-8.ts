class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let seen: {[key:string]: string[]} = {}
        strs.forEach((value) => {
            
            const sorted = value.split('').sort().join('')
            const isSeen = seen[sorted]
            if (!isSeen) {
                seen[sorted] = [value]
            } else {
                seen[sorted].push(value)
            }
        })

        console.log(Object.values(seen))
        return Object.values(seen)
    }
}
