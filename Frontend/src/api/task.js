import axios from './http'

const task ={
    getTaskData(){
        return axios.get('/task')
    },
    
    delTaskData(params){
        return axios.delete('/task',{params})
    },
    
    addTask(params){
        return axios.post('/task',params)
    }
}
export default task