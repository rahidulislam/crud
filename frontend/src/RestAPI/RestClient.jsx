import axios from 'axios'
export default class RestClent{
    static getUrl=(appUrl)=>{
        return axios.get(appUrl).then(response=>{
            return response.data
        }).catch(error=>{
            return console.log(error)
        })
    }
}