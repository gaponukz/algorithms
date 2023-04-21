// https://www.eolymp.com/uk/submissions/13561427
#include <iostream>
#include <vector>
using namespace std;

class TreeNode {
    public:
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Tree{
    public:
        TreeNode *head;
        Tree() : head(NULL) {}
        void Insert(int val) {
            if (head == NULL) {
                head = new TreeNode(val);
                return;
            }

            TreeNode *curr = head;

            while (curr != NULL) {
                if (val == curr->val) {
                    if (curr->right == NULL) {
                        curr->right = new TreeNode(val);
                        return;
                    }
                    else {
                        curr = curr->right;
                    }
                }
                else if (val < curr->val) {
                    if (curr->left == NULL) {
                        curr->left = new TreeNode(val);
                        return;
                    }
                    else {
                        curr = curr->left;
                    }
                } else {
                    if (curr->right == NULL) {
                        curr->right = new TreeNode(val);
                        return;
                    } else {
                        curr = curr->right;
                    }
                }
            }
        }

        bool IsSameTree(Tree *p) {
            return IsSameTreeHelper(head, p->head);
        }

    private:
        bool IsSameTreeHelper(TreeNode *node1, TreeNode *node2) {
            if (node1 == NULL && node2 == NULL) {
                return true;

            } else if (node1 == NULL || node2 == NULL) {
                return false;

            } else {
                return (node1->val == node2->val) &&
                IsSameTreeHelper(node1->left, node2->left) &&
                IsSameTreeHelper(node1->right, node2->right);
            }
        }
};


int main() {
    int n, m;
    cin >> n;
    vector<int> arr1(n);

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }
    
    cin >> m;
    vector<int> arr2(m);
    
    for (int i = 0; i < m; i++) {
        cin >> arr2[i];
    }

    Tree tree1, tree2;
    
    for (int i = 0; i < n; i++) {
        tree1.Insert(arr1[i]);
    }

    for (int i = 0; i < m; i++) {
        tree2.Insert(arr2[i]);
    }

    if (tree1.IsSameTree(&tree2)) {
        cout << "1" << endl;
    }
    else {
        cout << "0" << endl;
    }

    return 0;
}