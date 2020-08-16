import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Random;
import java.util.StringTokenizer;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Solution {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TheCrazyHelix solver = new TheCrazyHelix();
        solver.solve(1, in, out);
        out.close();
    }
}

class TheCrazyHelix {

    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int n = in.nextInt();
        int q = in.nextInt();
        Treap t = null;
        snapshot = new int[n];
        int[] inv = new int[n];
        for (int i = 0; i < n; i++) {
            t = insert(t, i, i);
            inv[i] = i;
        }
        final int MAX_CNT = 300;
        int[] left = new int[MAX_CNT];
        int[] right = new int[MAX_CNT];
        int cnt = 0;

        for (int i = 0; i < q; i++) {
            char type = in.next().charAt(0);
            if (type == '1') {
                int l = in.nextInt() - 1;
                int r = in.nextInt() - 1;
                t = reverse(t, l, r);
                left[cnt] = l;
                right[cnt] = r;
                ++cnt;
                if (cnt == MAX_CNT) {
                    pos = 0;
                    traverse(t);
                    for (int j = 0; j < n; j++) {
                        inv[snapshot[j]] = j;
                    }
                    cnt = 0;
                }
            } else if (type == '2') {
                int x = in.nextInt() - 1;
                int cur = inv[x];
                for (int j = 0; j < cnt; j++)
                    if (left[j] <= cur && cur <= right[j])
                        cur = left[j] + right[j] - cur;
                out.println("element " + (x + 1) + " is at position " + (cur + 1));
            } else {
                int y = in.nextInt() - 1;
                out.println("element at position " + (y + 1) + " is " + (kth(t, y) + 1));
            }
        }
    }

    static Random random = new Random();

    static void push(Treap root) {
        if (root == null || !root.reverse)
            return;
        Treap tmp = root.left;
        root.left = root.right;
        root.right = tmp;
        if (root.left != null)
            root.left.reverse = !root.left.reverse;
        if (root.right != null)
            root.right.reverse = !root.right.reverse;
        root.reverse = false;
    }

    static class Treap {
        final int value;
        boolean reverse;
        int size;
        final long prio;
        Treap left;
        Treap right;

        Treap(int value) {
            this.value = value;
            size = 1;
            prio = random.nextLong();
        }

        void update() {
            size = 1 + getSize(left) + getSize(right);
        }
    }

    static int getSize(Treap root) {
        return root == null ? 0 : root.size;
    }

    static class TreapPair {
        Treap left;
        Treap right;

        TreapPair(Treap left, Treap right) {
            this.left = left;
            this.right = right;
        }
    }

    static TreapPair split(Treap root, int minRight) {
        if (root == null)
            return new TreapPair(null, null);
        push(root);
        if (getSize(root.left) >= minRight) {
            TreapPair sub = split(root.left, minRight);
            root.left = sub.right;
            root.update();
            sub.right = root;
            return sub;
        } else {
            TreapPair sub = split(root.right, minRight - getSize(root.left) - 1);
            root.right = sub.left;
            root.update();
            sub.left = root;
            return sub;
        }
    }

    static Treap merge(Treap left, Treap right) {
        push(left);
        push(right);
        if (left == null)
            return right;
        if (right == null)
            return left;
        if (left.prio > right.prio) {
            left.right = merge(left.right, right);
            left.update();
            return left;
        } else {
            right.left = merge(left, right.left);
            right.update();
            return right;
        }
    }

    static Treap reverse(Treap root, int a, int b) {
        TreapPair t1 = split(root, b + 1);
        TreapPair t2 = split(t1.left, a);
        if (t2.right != null)
            t2.right.reverse = !t2.right.reverse;
        return merge(merge(t2.left, t2.right), t1.right);
    }


    static Treap insert(Treap root, int index, int value) {
        TreapPair t = split(root, index);
        return merge(merge(t.left, new Treap(value)), t.right);
    }

    static int kth(Treap root, int k) {
        push(root);
        if (k < getSize(root.left))
            return kth(root.left, k);
        else if (k > getSize(root.left))
            return kth(root.right, k - getSize(root.left) - 1);
        return root.value;
    }

    static int[] snapshot;
    static int pos;

    static void traverse(Treap root) {
        if (root == null)
            return;
        push(root);
        traverse(root.left);
        snapshot[pos++] = root.value;
        traverse(root.right);
    }
}

class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;

    public InputReader(InputStream stream) {
        reader = new BufferedReader(new InputStreamReader(stream));
    }

    public String next() {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
                tokenizer = new StringTokenizer(reader.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tokenizer.nextToken();
    }

    public int nextInt() {
        return Integer.parseInt(next());
    }
}