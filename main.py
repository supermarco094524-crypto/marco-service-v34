<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marco Service - Premium Diamond Top-up</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0a0f1e; color: #ffffff; font-family: 'Pyidaungsu', sans-serif; }
        .gold-text { color: #d4af37; }
        .premium-card { background: linear-gradient(145deg, #161f33, #0f172a); border: 1px solid #1e293b; transition: 0.3s; }
        .premium-card:hover { border-color: #d4af37; transform: translateY(-5px); }
        .btn-gold { background-color: #d4af37; color: #000; font-weight: bold; }
    </style>
</head>
<body>
    <header class="p-6 flex justify-between items-center border-b border-slate-800">
        <h1 class="text-2xl font-bold gold-text underline">MARCO SERVICE</h1>
        <div id="user-greeting" class="text-sm">မင်္ဂလာရှိသော နေ့လေးပါရှင့်!</div>
    </header>

    <div class="bg-blue-900/20 p-4 text-center text-xs gold-text">
        ဝန်ဆောင်မှုအချိန် - မနက် ၉:၀၀ နာရီ မှ ည ၁၁:၀၀ နာရီ ထိ ရှင့်
    </div>

    <section class="p-6">
        <div class="premium-card p-4 rounded-xl flex justify-between items-center">
            <div>
                <p class="text-gray-400 text-xs">လက်ကျန်ငွေ (Wallet)</p>
                <p class="text-xl font-bold">0 <span class="text-xs">Ks</span></p>
            </div>
            <button class="btn-gold px-4 py-2 rounded-lg text-sm">ငွေဖြည့်မည်</button>
        </div>
    </section>

    <section class="p-6 pt-0">
        <h2 class="text-lg font-bold mb-4">Shop - Diamond ဝယ်ယူရန်</h2>
        <div class="grid grid-cols-2 gap-4">
            <div class="premium-card p-4 rounded-xl border-l-4 border-l-sky-400" onclick="openOrder('Weekly Pass', 3000)">
                <p class="text-[10px] text-sky-400 font-bold uppercase">Weekly</p>
                <p class="text-sm font-bold">Weekly Pass</p>
                <p class="text-xs gold-text mt-2">3,000 Ks</p>
            </div>
            <div class="premium-card p-4 rounded-xl border-l-4 border-l-yellow-500" onclick="openOrder('80 Diamonds', 1400)">
                <p class="text-[10px] text-yellow-500 font-bold uppercase">Normal</p>
                <p class="text-sm font-bold">80 Diamonds</p>
                <p class="text-xs gold-text mt-2">1,400 Ks</p>
            </div>
        </div>
    </section>

    <div id="orderModal" class="fixed inset-0 bg-black/80 hidden p-6 z-50 overflow-y-auto">
        <div class="bg-slate-900 p-6 rounded-2xl border border-slate-700 max-w-md mx-auto">
            <h3 class="text-lg font-bold gold-text mb-4">အော်ဒါတင်ရန်</h3>
            <div class="space-y-4">
                <input type="text" placeholder="User ID" class="w-full bg-slate-800 p-3 rounded-lg border border-slate-700 outline-none">
                <input type="text" placeholder="Zone ID" class="w-full bg-slate-800 p-3 rounded-lg border border-slate-700 outline-none">
                <div class="bg-blue-900/10 p-4 rounded-lg text-xs border border-blue-800">
                    <p>KPay: 0989482838 (Thar Htoo Aung)</p>
                    <p>Wave: 0989482838 (Hla Min Aung)</p>
                </div>
                <label class="block text-xs text-gray-400">ငွေလွှဲပြေစာ (Screenshot) တင်ပေးပါ</label>
                <input type="file" class="w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-yellow-500 file:text-black">
                <button class="w-full btn-gold py-4 rounded-xl mt-4">အော်ဒါတင်မည် (Confirm)</button>
                <button onclick="document.getElementById('orderModal').classList.add('hidden')" class="w-full text-gray-400 text-sm py-2">ပိတ်မည်</button>
            </div>
        </div>
    </div>

    <script>
        function openOrder(item, price) {
            document.getElementById('orderModal').classList.remove('hidden');
        }
    </script>
</body>
</html>
