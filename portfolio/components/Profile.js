import {  Image } from 'antd';
const Profile = () => (
  <>
  <div className="container mx-auto">
    <div className="w-3/5 bg-gray-400 flex justify-around h-auto">
      <div className='w-1/3 bg-red-800 h-auto '>
      <Image className='self-center'
        width={300}
        src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"
     />
      </div>
      <div className='w-2/3 bg-red-500 h-auto'>2</div>
    </div>
  </div>
  </>
);
export default Profile;