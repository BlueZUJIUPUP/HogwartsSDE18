import axios from './http'

const task ={
    getTaskData(){
        return axios.get('/task')
    },
    createCase(params){
        return axios.post('/testcase',params)
    },
}
export default task