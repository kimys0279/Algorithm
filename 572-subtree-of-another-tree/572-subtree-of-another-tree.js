/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    if (!root) return !subRoot;
    return isEqual(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);    
};

function isEqual(r1, r2) {
    if (!r1 || !r2) return !r1 && !r2;
    if (r1.val !== r2.val) return false;
    return isEqual(r1.left, r2.left) && isEqual(r1.right, r2.right);
}