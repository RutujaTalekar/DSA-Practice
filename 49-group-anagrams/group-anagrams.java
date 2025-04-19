class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anags = new HashMap<>();
        for(int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            if (!anags.containsKey(sorted)) {
                anags.put(sorted, new ArrayList<String>());
            }
            // System.out.println(anags);
            anags.get(sorted).add(strs[i]);
        }

        return new ArrayList(anags.values());
    }
}