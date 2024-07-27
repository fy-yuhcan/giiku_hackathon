import React, { useEffect, useState } from 'react';

interface FoodItem {
  name: string;
  quantity: string | number;
  unit: string;
}

const mockData: FoodItem[] = [
  { name: 'とりもも', quantity: 200, unit: 'g' },
  { name: 'にんじん', quantity: 1, unit: '個' },
  { name: 'ソーセージ', quantity: 2, unit: '袋' },
  { name: 'バナナ', quantity: 5, unit: '本' },
  { name: '食パン', quantity: 6, unit: '枚' },
  { name: 'しめじ', quantity: 1, unit: 'パック' },
  { name: 'とりもも', quantity: 200, unit: 'g' },
  { name: 'にんじん', quantity: 1, unit: '個' },
  { name: 'ソーセージ', quantity: 2, unit: '袋' },
  { name: 'バナナ', quantity: 5, unit: '本' },
  { name: '食パン', quantity: 6, unit: '枚' },
  { name: 'しめじ', quantity: 1, unit: 'パック' },
];

export default function FridgeComponent() {
  const [foodItems, setFoodItems] = useState<FoodItem[]>([]);

  useEffect(() => {
    // 実際にはデータベースからデータをフェッチします
    // fetch('/api/food-items')
    //   .then(response => response.json())
    //   .then(data => setFoodItems(data));
    setFoodItems(mockData);
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-cream-light">
      <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-4xl mx-auto mt-10">
        <h1 className="text-center text-xl font-semibold mb-4">家にある食材</h1>
        <div className="bg-white p-4 rounded-md shadow-sm max-h-96 overflow-y-auto">
          <table className="min-w-full">
            <thead>
              <tr>
                <th className="border-b-2 border-gray-300 p-4 text-left">食材名</th>
                <th className="border-b-2 border-gray-300 p-4 text-right">数</th>
                <th className="border-b-2 border-gray-300 p-4 text-left">単位</th>
              </tr>
            </thead>
            <tbody>
              {foodItems.map((item, index) => (
                <tr key={index}>
                  <td className="border-b border-gray-200 p-4">{item.name}</td>
                  <td className="border-b border-gray-200 p-4 text-right">{item.quantity}</td>
                  <td className="border-b border-gray-200 p-4">{item.unit}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
