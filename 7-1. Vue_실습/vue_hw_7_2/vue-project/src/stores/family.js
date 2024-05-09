import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useFamilyStore = defineStore('family', () => {

    const familyInfo = ref([
        { 
            familyName: '메디치', 
            father: '로도비코 데 메디치', 
            mother: '마리아 살비아티',
            children: [{ name: '틀레도의 엘 레오노르' }, { name: '코시모 1세' }]
        },
        { 
            fmilyName: '전주 이씨',
            father: '이도',
            mother: '소헌왕후',
            children: [{ name: '이향' }, { name: '이유' }]
        }]

    )

    return { familyInfo }
})