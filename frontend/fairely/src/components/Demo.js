import React from 'react'

export default function Demo() {
  
  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("/get-product-details").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					name: data.Name,
					age: data.Age,
					date: data.Date,
					programming: data.programming,
				});
			})
		);
    console.log('Submitted');
    }

  return (
    <>
        <div className="container py-5">
            
            <h1 className='mb-4'>Demo</h1>

            <form onSubmit={handleSubmit}>
                <div className='d-flex justify-content-center'>
                    <h4 className='text-lg-start mx-3'>URL: </h4>
                    <input type="text" class="form-control w-25" id="inputPassword" placeholder="Enter your URL"/>
                </div>
                <div className='d-flex justify-content-center my-3'>
                    <button type="submit" class="btn btn-primary mt-3">Submit</button>
                </div>
            </form>
        </div>
    </>
  )
}
