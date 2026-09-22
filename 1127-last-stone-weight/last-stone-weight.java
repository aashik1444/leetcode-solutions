class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int s: stones) {
            heap.offer(-s);
        }
        while (heap.size() > 1) {
            int f = heap.poll();
            int s = heap.poll();
            if (s > f) {
                heap.offer(f - s);
            }
        }
        heap.offer(0);
        return Math.abs(heap.peek());
    }
}