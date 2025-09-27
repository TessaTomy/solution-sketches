// rotate_array_buffer.c
// Approach: Copy rotated result into temp, then overwrite original

void rotate(int* nums, int numsSize, int k) {
    k = k % numsSize;
    int* temp = (int*)malloc(sizeof(int) * numsSize);

    for (int i = 0; i < numsSize; i++) {
        temp[(i + k) % numsSize] = nums[i];
    }

    for (int i = 0; i < numsSize; i++) {
        nums[i] = temp[i];
    }

    free(temp);
}
