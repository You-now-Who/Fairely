import React from 'react'

export default function Home() {
  return (
    <>
        <div className="px-4 py-5 text-center">
        <img className="d-block mx-auto mb-4" src="https://cdn-icons-png.flaticon.com/512/5952/5952839.png" alt="" width="256" height="256"/>
        <h1 className="display-5 fw-bold">Fairely</h1>
        <div className="col-lg-6 mx-auto">
        <p className="lead mb-4">Helping you avoid pitfalls in your online shopping journey</p>
        <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            <button type="button" className="btn btn-primary btn-lg px-4 gap-3">Check out live demo</button>
            {/* <button type="button" className="btn btn-outline-secondary btn-lg px-4">Secondary</button> */}
        </div>
        </div>
    </div>
    
    <div className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5 px-4">
    
      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" style={{backgroundImage: `linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0, 0.9)), url('https://static.doofinder.com/main-files/uploads/2020/05/Ideas-crear-tienda-online.jpg')`}}>
          <div className="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
            <h3 className=" mt-5 mb-4 display-6 lh-1 fw-bold">Identify fake reviews at the click of a button</h3>
            <ul className="d-flex list-unstyled mt-auto">
              {/* <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li> */}
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" style={{backgroundImage: `url('https://cdn.pixabay.com/photo/2018/03/27/10/03/online-store-3265497_1280.jpg')`}}>
          <div className="d-flex flex-column h-100 p-5 pb-3 text-dark text-shadow-1">
            <h3 className=" mt-5 mb-4 display-6 lh-1 fw-bold">Get notified of scam websites</h3>
            <ul className="d-flex list-unstyled mt-auto">
              {/* <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li> */}
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg" style={{backgroundImage: `url('https://cdn.vox-cdn.com/thumbor/7r4x0NYGEPpJIB-oRInSlCEJvoo=/0x0:2040x1360/1200x628/filters:focal(1020x680:1021x681)/cdn.vox-cdn.com/uploads/chorus_asset/file/10581347/acastro_180321_1777_youtube_0002.jpg')`}}>
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h3 className=" mt-5 mb-4 display-6 lh-1 fw-bold">Have top Youtube reviews and caveats at your fingertips</h3>
            <ul className="d-flex list-unstyled mt-auto">
              {/* <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"/>
              </li> */}
            </ul>
          </div>
        </div>
      </div>
    </div>
    </>
  )
}
