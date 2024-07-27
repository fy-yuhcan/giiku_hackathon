import React, { useState, useRef } from 'react';
import useSWRMutation from 'swr/mutation';
import { FoodDataType } from '../materialType';

export default function Picture({setFoodData}) {

  const DetectionFoodImagePath = "/storage/img/";

  async function uploadImage(url: string, { arg }) {
    const formData = new FormData();
    formData.append('upload_file', arg.file);
    //写真をバックエンドに保存するapiにアクセス
    fetch(url, {
      method: "POST",
      body: formData,
    })
      .then(res => res.json());
  }


  const handleChangeFoodData = (newFoodData: FoodDataType[]) => {
    setFoodData(newFoodData)
  }

  const { trigger, data, error } = useSWRMutation("/fridge", uploadImage);

  const [previewSrc, setPreviewSrc] = useState(null);
  const fileInputRef = useRef(null);

  const handleChangeFile = async (event: React.ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    const file = event.target.files[0];
    if (file) {
      setPreviewSrc(URL.createObjectURL(file));
      try {
        const result = await trigger({ file });
      } catch (e) {
        console.log(e);
      }
      if (data) {
        handleChangeFoodData(data)
      }
    }
  };

  const handleDrop = async (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      setPreviewSrc(URL.createObjectURL(file));
      fileInputRef.current.files = event.dataTransfer.files;
      await trigger({ file });
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <div
        className="border-2 border-gray-300 p-4 rounded-md w-full h-64 flex items-center justify-center"
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
      >
        {previewSrc ? (
          <img src={previewSrc} alt="Preview" className="max-h-full max-w-full" />
        ) : (
          <span className="text-gray-400">写真をドロップ</span>
        )}
      </div>
      <input
        type='file'
        ref={fileInputRef}
        onChange={(event) => handleChangeFile(event)}
        className="mt-4"
      />
    </div>
  );
}
