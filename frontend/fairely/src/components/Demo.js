import React, {useState, useEffect} from 'react'

export default function Demo() {
  
  const [domain, setDomain] = useState('');
  const [content, setContent] = useState('');

  const fetchData = () => {
        fetch("/get-reviews").then((res) =>
                res.json().then((data) => {
                    // Setting a data from api
                    setDomain(data.domain);
                })
            );
    
    return;
    
  }

  

   const handleSubmit = (e) => {
    e.preventDefault();
    
    let data = new FormData();
    data.append('url', content);

    const requestOptions={
        method:"POST",
        mode:"no-cors",
        body:data,
        headers:{
            'content-type':'application/json'
        }
    }

    console.log(content)

    // send a post request to the backend at /set-url
    fetch('http://localhost:5000/set-url', requestOptions)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))




    // fetchData();
   }
   
   useEffect(() => {
     fetchData();
   }, []);

  return (
    <>
        <div className="container py-5">
            
            <h1 className='mb-4'>Demo</h1>

            <form>
                <div className='d-flex justify-content-center'>
                    <h4 className='text-lg-start mx-3'>URL: </h4>
                    <input type="text" className="form-control w-25" id="url" placeholder="Enter your URL" value={content} onChange={e => setContent(e.target.value)}/>
                </div>
                <div className='d-flex justify-content-center my-3'>
                    <button type="submit" className="btn btn-primary mt-3" onClick={handleSubmit}>Submit</button>

                    {/* <button type="submit" value="Add Todo"
                    onClick={handleSubmit}>
                        </button> */}
                </div>
            </form>
            {/* <h1>{{domain}}</h1> */}
        </div>
    </>
  )
}
