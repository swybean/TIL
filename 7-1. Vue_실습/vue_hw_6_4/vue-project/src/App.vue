<template>
  <div>
    <MainPage />

    <RouterLink :to="{ name: 'some' }">Some</RouterLink> |

    <RouterLink :to="{ name: 'other' }">Other</RouterLink> |

    <RouterLink :to="{ name: 'students' }">Students</RouterLink> |

    <!-- <RouterLink :to="{ name: 'detail', params: {'name': studentName} }">Name</RouterLink> -->
    <!-- 얘는 라우터.푸시를 사용하니까 사용하지 않아도된다. -->
    <RouterView />
  </div>


</template>



<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

import MainPage from '@/components/MainPage.vue'

const studentName = ref('김하나')


</script>



<style scoped>


</style>
