import axios from './http'

const cases ={
    getCaseList(params){
        return axios.get('/testcase',{params})
    },
    createCase(params){
        return axios.post('/testcase',params)
    },
    deleteCase(params){
        return axios.delete('/testcase',{params})
    },
    updateCase(params){
        return axios.put('/testcase',params)
    },
    // createFileCase(params){
    //     return axios.post('/testCase/file',params)
    // },
}
export default cases