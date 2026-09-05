// ⚡ Lightning Expo 2026 - 主控台腳本

document.addEventListener('DOMContentLoaded', () => {
    console.log('⚡ AI × OPER × BOT Expo 2026 已啟動');
    console.log('📍 臺中國際會展中心 (TICEC)');
    console.log('📅 2026/09/08 – 2026/09/13');
    console.log('🔐 核心原則：AI 建議 → 人類確認 → 授權 BOT 執行');

    // 卡片點擊效果（展示用）
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.addEventListener('click', () => {
            const title = card.querySelector('h3')?.innerText || '區塊';
            console.log(`🔍 點擊展示區：${title}`);
            // 簡單視覺反饋
            card.style.borderColor = '#f5a623';
            setTimeout(() => {
                card.style.borderColor = '#1e2636';
            }, 600);
        });
    });

    // 狀態標示點擊顯示提醒
    const badges = document.querySelectorAll('.badge');
    badges.forEach(badge => {
        badge.addEventListener('click', () => {
            const text = badge.innerText;
            alert(`🛡️ 狀態標示：${text}\n（本展示為模擬／概念驗證，不對外控制任何第三方系統）`);
        });
    });

    // 顯示展覽倒數（僅供參考）
    const targetDate = new Date('2026-09-08T00:00:00');
    const now = new Date();
    const diff = targetDate - now;
    if (diff > 0) {
        const days = Math.ceil(diff / (1000 * 60 * 60 * 24));
        console.log(`⏳ 距離展覽開幕還有 ${days} 天`);
    } else {
        console.log('🚀 展覽已開始！');
    }
});
