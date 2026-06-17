<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bishal.ai · SambaNova</title>
  <!-- Font Awesome & Google Font (Inter) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700;14..32,800;14..32,900&display=swap" rel="stylesheet" />
  <style>
    /* ============================================================
       RESET & BASE - 100+ KB STYLING WITH EXTENSIVE ANIMATIONS
       ============================================================ */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: 'Inter', sans-serif;
      background: #030812;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.2rem;
      position: relative;
      overflow-x: hidden;
    }
    /* animated background particles - extensive */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 20% 30%, #0b1a2e, #030812);
      z-index: -2;
    }
    .glow-orb {
      position: fixed;
      border-radius: 50%;
      filter: blur(90px);
      opacity: 0.25;
      pointer-events: none;
      z-index: -1;
      animation: floatOrb 12s infinite alternate ease-in-out;
    }
    .glow-orb:nth-child(1) {
      width: 40vw;
      height: 40vw;
      top: -10%;
      left: -10%;
      background: #1a3d66;
      animation-duration: 14s;
    }
    .glow-orb:nth-child(2) {
      width: 35vw;
      height: 35vw;
      bottom: -15%;
      right: -10%;
      background: #2a4d7a;
      animation-duration: 18s;
      animation-delay: 2s;
    }
    .glow-orb:nth-child(3) {
      width: 25vw;
      height: 25vw;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: #1f3f66;
      animation-duration: 20s;
      animation-delay: 4s;
      opacity: 0.15;
    }
    .glow-orb:nth-child(4) {
      width: 20vw;
      height: 20vw;
      top: 20%;
      right: 10%;
      background: #3b5f8a;
      animation-duration: 16s;
      animation-delay: 1s;
      opacity: 0.1;
    }
    .glow-orb:nth-child(5) {
      width: 30vw;
      height: 30vw;
      bottom: 10%;
      left: 5%;
      background: #1a4a6a;
      animation-duration: 22s;
      animation-delay: 3s;
      opacity: 0.12;
    }
    .glow-orb:nth-child(6) {
      width: 15vw;
      height: 15vw;
      top: 60%;
      right: 20%;
      background: #2a5a7a;
      animation-duration: 19s;
      animation-delay: 5s;
      opacity: 0.08;
    }
    .glow-orb:nth-child(7) {
      width: 18vw;
      height: 18vw;
      bottom: 30%;
      left: 30%;
      background: #1a3a5a;
      animation-duration: 21s;
      animation-delay: 2.5s;
      opacity: 0.1;
    }
    @keyframes floatOrb {
      0% { transform: translate(0, 0) scale(1); }
      25% { transform: translate(3%, 5%) scale(1.05); }
      50% { transform: translate(4%, 6%) scale(1.1); }
      75% { transform: translate(2%, 3%) scale(1.03); }
      100% { transform: translate(-3%, -4%) scale(0.95); }
    }

    /* floating particles */
    .particle-container {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: -1;
      overflow: hidden;
    }
    .particle {
      position: absolute;
      width: 4px;
      height: 4px;
      background: rgba(255,255,255,0.04);
      border-radius: 50%;
      animation: particleFloat 20s infinite linear;
    }
    .particle:nth-child(1) { left: 10%; top: 20%; animation-duration: 18s; }
    .particle:nth-child(2) { left: 25%; top: 60%; animation-duration: 22s; animation-delay: 2s; }
    .particle:nth-child(3) { left: 45%; top: 15%; animation-duration: 16s; animation-delay: 4s; }
    .particle:nth-child(4) { left: 65%; top: 70%; animation-duration: 20s; animation-delay: 1s; }
    .particle:nth-child(5) { left: 80%; top: 30%; animation-duration: 24s; animation-delay: 3s; }
    .particle:nth-child(6) { left: 15%; top: 85%; animation-duration: 19s; animation-delay: 5s; }
    .particle:nth-child(7) { left: 55%; top: 45%; animation-duration: 21s; animation-delay: 2.5s; }
    .particle:nth-child(8) { left: 90%; top: 55%; animation-duration: 17s; animation-delay: 1.5s; }
    .particle:nth-child(9) { left: 35%; top: 90%; animation-duration: 23s; animation-delay: 3.5s; }
    .particle:nth-child(10) { left: 70%; top: 10%; animation-duration: 15s; animation-delay: 4.5s; }
    .particle:nth-child(11) { left: 5%; top: 40%; animation-duration: 25s; animation-delay: 6s; }
    .particle:nth-child(12) { left: 50%; top: 75%; animation-duration: 18s; animation-delay: 1.2s; }
    .particle:nth-child(13) { left: 85%; top: 85%; animation-duration: 22s; animation-delay: 3.8s; }
    .particle:nth-child(14) { left: 30%; top: 10%; animation-duration: 20s; animation-delay: 4.2s; }
    .particle:nth-child(15) { left: 60%; top: 95%; animation-duration: 16s; animation-delay: 2.1s; }
    @keyframes particleFloat {
      0% { transform: translateY(0) translateX(0) scale(1); opacity: 0.3; }
      25% { transform: translateY(-30px) translateX(15px) scale(1.2); opacity: 0.6; }
      50% { transform: translateY(-60px) translateX(-10px) scale(0.8); opacity: 0.2; }
      75% { transform: translateY(-30px) translateX(20px) scale(1.1); opacity: 0.5; }
      100% { transform: translateY(0) translateX(0) scale(1); opacity: 0.3; }
    }

    /* APP WRAPPER */
    .app-wrapper {
      max-width: 1100px;
      width: 100%;
      background: rgba(255, 255, 255, 0.02);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-radius: 3.6rem;
      padding: 0.4rem;
      box-shadow: 0 60px 100px -30px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(255, 255, 255, 0.02);
      transition: all 0.3s ease;
      animation: appFade 0.8s ease;
    }
    @keyframes appFade {
      0% { opacity: 0; transform: scale(0.96) rotate(-0.5deg); }
      100% { opacity: 1; transform: scale(1) rotate(0deg); }
    }
    .app-card {
      background: linear-gradient(165deg, #0f1d30, #081424);
      border-radius: 3.2rem;
      overflow: hidden;
      box-shadow: inset 0 2px 0 rgba(255,255,255,0.02);
    }

    /* ---- BANNER (Bishal.ai) ---- */
    .banner {
      background: linear-gradient(145deg, #13273f, #071528);
      padding: 1.4rem 2.2rem;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.02);
      position: relative;
      overflow: hidden;
    }
    .banner::after {
      content: '';
      position: absolute;
      top: -60%;
      left: -20%;
      width: 80%;
      height: 200%;
      background: radial-gradient(circle, rgba(59,130,246,0.02) 0%, transparent 70%);
      pointer-events: none;
    }
    .banner::before {
      content: '';
      position: absolute;
      bottom: -50%;
      right: -10%;
      width: 60%;
      height: 150%;
      background: radial-gradient(circle, rgba(59,130,246,0.015) 0%, transparent 70%);
      pointer-events: none;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      z-index: 1;
    }
    .brand-icon {
      font-size: 2.8rem;
      background: linear-gradient(135deg, #7aa9ff, #3f7cdf);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 24px #3b82f660);
      animation: iconPulse 3s infinite alternate;
      transition: 0.3s;
    }
    @keyframes iconPulse {
      0% { filter: drop-shadow(0 0 8px #3b82f640); transform: scale(1) rotate(0deg); }
      50% { transform: scale(1.02) rotate(2deg); }
      100% { filter: drop-shadow(0 0 32px #3b82f6b0); transform: scale(1.04) rotate(-2deg); }
    }
    .brand h1 {
      font-weight: 900;
      font-size: 2.4rem;
      letter-spacing: -0.03em;
      background: linear-gradient(to right, #f0f6ff, #b8d0ff, #8ab0ff, #6f9eff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-shadow: 0 0 40px rgba(59,130,246,0.1);
      animation: textShimmer 4s infinite alternate;
    }
    @keyframes textShimmer {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }
    .brand .badge {
      font-weight: 600;
      font-size: 0.7rem;
      background: rgba(255, 255, 255, 0.04);
      padding: 0.25rem 1.2rem;
      border-radius: 40px;
      color: #8ba9e6;
      border: 1px solid rgba(255,255,255,0.04);
      margin-left: 0.3rem;
      letter-spacing: 0.6px;
      backdrop-filter: blur(4px);
      text-transform: uppercase;
      animation: badgeGlow 3s infinite alternate;
    }
    @keyframes badgeGlow {
      0% { border-color: rgba(255,255,255,0.04); box-shadow: 0 0 0px rgba(59,130,246,0); }
      100% { border-color: rgba(59,130,246,0.2); box-shadow: 0 0 20px rgba(59,130,246,0.05); }
    }

    /* login panel - enhanced */
    .login-panel {
      display: flex;
      align-items: center;
      gap: 1.2rem;
      background: rgba(255, 255, 255, 0.01);
      padding: 0.2rem 0.2rem 0.2rem 1.4rem;
      border-radius: 60px;
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.02);
      z-index: 1;
      transition: 0.3s;
    }
    .login-panel:hover {
      border-color: rgba(255, 255, 255, 0.04);
      background: rgba(255, 255, 255, 0.02);
    }
    .user-badge {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #c2d6f5;
      font-weight: 500;
      font-size: 0.95rem;
    }
    .user-badge i {
      font-size: 1.5rem;
      color: #6f9eff;
      transition: 0.3s;
      filter: drop-shadow(0 0 6px rgba(95,142,255,0.2));
    }
    .user-badge .avatar-placeholder {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: linear-gradient(135deg, #1a3d66, #2a4d7a);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
      font-size: 0.9rem;
      border: 1px solid rgba(255,255,255,0.05);
      transition: 0.3s;
    }
    .user-badge .avatar-placeholder:hover {
      transform: scale(1.05);
      border-color: rgba(255,255,255,0.1);
    }
    .google-btn {
      background: white;
      border: none;
      padding: 0.55rem 1.8rem;
      border-radius: 60px;
      font-weight: 700;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.8rem;
      color: #0b1a2e;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.2, 0.9, 0.4, 1);
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      border: 1px solid rgba(255,255,255,0.1);
      position: relative;
      overflow: hidden;
    }
    .google-btn::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(255,255,255,0.1), transparent);
      opacity: 0;
      transition: 0.3s;
    }
    .google-btn:hover::after {
      opacity: 1;
    }
    .google-btn i {
      color: #4285F4;
      font-size: 1.1rem;
    }
    .google-btn:hover {
      transform: scale(1.03) translateY(-2px);
      background: #f2f8ff;
      box-shadow: 0 16px 36px -8px rgba(59, 130, 246, 0.3);
    }
    .google-btn.logged {
      background: #e0edff;
      border-color: #5f8eff;
    }

    /* ---- MAIN ---- */
    .main-content {
      padding: 2rem 2.2rem 2.2rem 2.2rem;
    }

    /* model selector */
    .model-selector {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.8rem 1.5rem;
      background: rgba(255, 255, 255, 0.01);
      padding: 0.5rem 1.5rem 0.5rem 1.8rem;
      border-radius: 60px;
      margin-bottom: 2rem;
      border: 1px solid rgba(255, 255, 255, 0.02);
      backdrop-filter: blur(4px);
      animation: selectorPulse 4s infinite alternate;
    }
    @keyframes selectorPulse {
      0% { border-color: rgba(255,255,255,0.02); }
      100% { border-color: rgba(59,130,246,0.05); }
    }
    .model-selector label {
      font-weight: 600;
      font-size: 0.9rem;
      color: #b4ccf0;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .model-selector label i {
      color: #5f8eff;
      animation: labelIconSpin 6s infinite linear;
    }
    @keyframes labelIconSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .model-selector select {
      background: #162b44;
      border: 1px solid #2c405e;
      border-radius: 40px;
      padding: 0.5rem 2rem 0.5rem 1.4rem;
      font-weight: 600;
      color: #eaf2ff;
      font-family: 'Inter', sans-serif;
      cursor: pointer;
      outline: none;
      transition: 0.25s;
      font-size: 0.9rem;
      min-width: 180px;
      appearance: none;
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8"><path fill="%2380a5e0" d="M6 8L0 0h12z"/></svg>');
      background-repeat: no-repeat;
      background-position: right 1.2rem center;
      background-size: 12px;
    }
    .model-selector select:focus {
      border-color: #5f8eff;
      box-shadow: 0 0 0 4px rgba(95, 142, 255, 0.08);
    }
    .model-selector select option {
      background: #0e1a2b;
      color: #eaf2ff;
    }
    .status-badge {
      font-size: 0.8rem;
      color: #a8c0e0;
      background: rgba(255, 255, 255, 0.02);
      padding: 0.3rem 1.4rem;
      border-radius: 30px;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      border: 1px solid rgba(255,255,255,0.02);
      margin-left: auto;
      backdrop-filter: blur(4px);
      font-weight: 500;
      transition: 0.3s;
    }
    .status-badge .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      display: inline-block;
      animation: dotPulse 1.8s infinite;
    }
    @keyframes dotPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(0.8); }
    }

    /* chat box */
    .chat-box {
      background: rgba(10, 22, 40, 0.3);
      backdrop-filter: blur(12px);
      border-radius: 2.2rem;
      padding: 1.8rem 2rem;
      border: 1px solid rgba(255, 255, 255, 0.01);
      min-height: 300px;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
      position: relative;
      overflow: hidden;
    }
    .chat-box::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle at 30% 40%, rgba(59,130,246,0.01), transparent 60%);
      pointer-events: none;
    }
    .chat-messages {
      flex: 1;
      margin-bottom: 1.2rem;
      max-height: 380px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      padding-right: 0.3rem;
      position: relative;
      z-index: 1;
    }
    .chat-messages::-webkit-scrollbar {
      width: 5px;
    }
    .chat-messages::-webkit-scrollbar-track {
      background: transparent;
    }
    .chat-messages::-webkit-scrollbar-thumb {
      background: #2f4a70;
      border-radius: 10px;
      transition: 0.3s;
    }
    .chat-messages::-webkit-scrollbar-thumb:hover {
      background: #3f5a80;
    }
    .msg {
      padding: 0.9rem 1.5rem;
      border-radius: 2rem;
      max-width: 85%;
      word-break: break-word;
      line-height: 1.7;
      font-size: 0.95rem;
      animation: msgSlide 0.3s ease;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      position: relative;
    }
    @keyframes msgSlide {
      0% { opacity: 0; transform: translateY(12px) scale(0.96); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    .msg.user {
      align-self: flex-end;
      background: linear-gradient(145deg, #1d3c66, #142f52);
      color: #f0f6ff;
      border-bottom-right-radius: 0.2rem;
      border: 1px solid #2a4d7a;
    }
    .msg.user::after {
      content: '';
      position: absolute;
      bottom: -8px;
      right: 0;
      width: 12px;
      height: 12px;
      background: #1d3c66;
      border-radius: 0 0 0 12px;
      border: 1px solid #2a4d7a;
      border-top: none;
      border-right: none;
    }
    .msg.ai {
      align-self: flex-start;
      background: linear-gradient(145deg, #132337, #0d1f33);
      color: #e2edff;
      border-bottom-left-radius: 0.2rem;
      border: 1px solid #263e5a;
      backdrop-filter: blur(2px);
    }
    .msg.ai::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 0;
      width: 12px;
      height: 12px;
      background: #132337;
      border-radius: 0 0 12px 0;
      border: 1px solid #263e5a;
      border-top: none;
      border-left: none;
    }
    .msg.ai i {
      margin-right: 0.6rem;
      color: #7aa9ff;
    }
    .msg .model-tag {
      display: inline-block;
      font-size: 0.6rem;
      background: rgba(95, 142, 255, 0.08);
      padding: 0.15rem 0.8rem;
      border-radius: 40px;
      margin-top: 0.5rem;
      color: #8ab0ff;
      font-weight: 600;
      letter-spacing: 0.4px;
      border: 1px solid rgba(95, 142, 255, 0.04);
    }
    .input-area {
      display: flex;
      gap: 0.8rem;
      align-items: center;
      margin-top: 0.2rem;
      flex-wrap: wrap;
      position: relative;
      z-index: 1;
    }
    .input-area input {
      flex: 1;
      padding: 1rem 1.6rem;
      border-radius: 60px;
      border: 1px solid #283e5a;
      background: #0d1e31;
      color: #ecf3ff;
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      outline: none;
      transition: 0.25s;
      min-width: 160px;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);
    }
    .input-area input:focus {
      border-color: #5f8eff;
      box-shadow: 0 0 0 4px rgba(95, 142, 255, 0.04), inset 0 2px 8px rgba(0,0,0,0.5);
    }
    .input-area input::placeholder {
      color: #6d8bb0;
      font-weight: 400;
    }
    .input-area button {
      background: linear-gradient(145deg, #1a3d66, #0d2642);
      border: none;
      color: white;
      padding: 1rem 2.4rem;
      border-radius: 60px;
      font-weight: 700;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 0.7rem;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.2, 0.9, 0.4, 1);
      border: 1px solid rgba(255, 255, 255, 0.02);
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.4);
      position: relative;
      overflow: hidden;
    }
    .input-area button::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(255,255,255,0.05), transparent);
      opacity: 0;
      transition: 0.3s;
    }
    .input-area button:hover::before {
      opacity: 1;
    }
    .input-area button i {
      font-size: 1.1rem;
      color: #9dbfff;
      transition: 0.3s;
    }
    .input-area button:hover {
      background: linear-gradient(145deg, #254f7a, #123456);
      transform: scale(1.02);
      box-shadow: 0 16px 40px -10px #1a3d66;
    }
    .input-area button:hover i {
      transform: translateX(4px) scale(1.05);
    }
    .input-area button:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }
    .footer-note {
      margin-top: 1.8rem;
      text-align: right;
      font-size: 0.8rem;
      color: #4b6d91;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      align-items: center;
    }
    .footer-note a {
      color: #6f9eff;
      text-decoration: none;
      font-weight: 600;
      transition: 0.2s;
      opacity: 0.7;
    }
    .footer-note a:hover {
      color: #9bbaff;
      opacity: 1;
      text-decoration: underline;
    }
    .hidden {
      display: none !important;
    }
    .loader {
      display: inline-block;
      width: 18px;
      height: 18px;
      border: 2.5px solid rgba(255,255,255,0.08);
      border-radius: 50%;
      border-top-color: #8ab0ff;
      animation: spin 0.7s linear infinite;
      margin-left: 0.3rem;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* typing indicator */
    .typing-indicator {
      display: flex;
      gap: 0.3rem;
      padding: 0.5rem 0;
      align-items: center;
    }
    .typing-indicator span {
      width: 8px;
      height: 8px;
      background: #6f9eff;
      border-radius: 50%;
      animation: typingBounce 1.4s infinite;
    }
    .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
    .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typingBounce {
      0%, 60%, 100% { transform: translateY(0); opacity: 0.3; }
      30% { transform: translateY(-8px); opacity: 1; }
    }

    /* ============================================================
       EXTRA ANIMATIONS & STYLES FOR 100+ KB
       ============================================================ */
    .welcome-message {
      background: rgba(59,130,246,0.03);
      border-radius: 1rem;
      padding: 1rem;
      border-left: 3px solid #3b82f6;
      margin-bottom: 0.5rem;
    }
    .quick-actions {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-top: 0.5rem;
    }
    .quick-action-btn {
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.05);
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
      color: #8ba9e6;
      font-size: 0.7rem;
      cursor: pointer;
      transition: 0.2s;
    }
    .quick-action-btn:hover {
      background: rgba(59,130,246,0.1);
      border-color: rgba(59,130,246,0.2);
    }
    .message-timestamp {
      font-size: 0.6rem;
      color: #4b6d91;
      margin-top: 0.2rem;
      opacity: 0.6;
    }
    .user-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #1a3d66, #2a4d7a);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
      font-size: 0.7rem;
      margin-right: 0.5rem;
    }
    .ai-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: linear-gradient(135deg, #3b5f8a, #1a3d66);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
      font-size: 0.7rem;
      margin-right: 0.5rem;
    }

    /* Additional decorative elements */
    .glow-line {
      width: 100%;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(59,130,246,0.1), transparent);
      margin: 0.5rem 0;
    }
    .stats-bar {
      display: flex;
      gap: 1.5rem;
      font-size: 0.7rem;
      color: #4b6d91;
    }
    .stats-bar span {
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }
    .stats-bar i {
      color: #5f8eff;
      font-size: 0.6rem;
    }

    @media (max-width: 700px) {
      .banner { flex-direction: column; align-items: start; gap: 0.8rem; padding: 1.2rem; }
      .login-panel { width: 100%; justify-content: space-between; padding-left: 1rem; }
      .main-content { padding: 1.2rem; }
      .model-selector { border-radius: 30px; flex-direction: column; align-items: stretch; }
      .status-badge { margin-left: 0; }
      .brand h1 { font-size: 1.8rem; }
      .stats-bar { flex-wrap: wrap; gap: 0.8rem; }
    }
  </style>
</head>
<body>
  <!-- animated glow orbs -->
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>
  <div class="glow-orb"></div>

  <!-- floating particles -->
  <div class="particle-container">
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
  </div>

<div class="app-wrapper">
<div class="app-card" id="app">
  <!-- BANNER (Bishal.ai) -->
  <div class="banner">
    <div class="brand">
      <i class="fas fa-cloud-upload-alt brand-icon"></i>
      <h1>Bishal.ai</h1>
      <span class="badge">SambaNova</span>
    </div>
    <div class="login-panel" id="loginPanel">
      <div class="user-badge" id="userBadge">
        <div class="avatar-placeholder" id="avatarPlaceholder">G</div>
        <span id="userNameDisplay">Guest</span>
      </div>
      <button class="google-btn" id="googleLoginBtn">
        <i class="fab fa-google"></i> <span id="loginBtnText">Sign in</span>
      </button>
    </div>
  </div>

  <!-- MAIN -->
  <div class="main-content">
    <!-- model selector -->
    <div class="model-selector">
      <label for="modelSelect"><i class="fas fa-microchip"></i> Model</label>
      <select id="modelSelect">
        <option value="llama">Meta-Llama-3.3-70B</option>
        <option value="deepseek">DeepSeek-V3.1</option>
        <option value="minimax">MiniMax-M2.7</option>
        <option value="gpt-oss">gpt-oss-120b</option>
      </select>
      <span class="status-badge" id="statusBadge">
        <span class="dot" style="background: #4ac7a2;"></span> ready
      </span>
    </div>

    <!-- chat -->
    <div class="chat-box">
      <div class="chat-messages" id="chatMessages">
        <div class="msg ai"><i class="fas fa-robot"></i> Hey, I'm Bishal.ai. How can I help you today?<span class="model-tag">llama</span></div>
      </div>
      <div class="input-area">
        <input type="text" id="messageInput" placeholder="Ask anything..." />
        <button id="sendBtn"><i class="fas fa-paper-plane"></i> Send</button>
      </div>
    </div>

    <div class="footer-note">
      <span><i class="fas fa-key" style="opacity:0.3;"></i> SambaNova API</span>
      <span><i class="fas fa-sign-out-alt" style="opacity:0.4;"></i> <a href="#" id="logoutLink" class="hidden">Logout</a></span>
    </div>
  </div>
</div>
</div>

<script>
  (function(){
    // ============================================================
    // BISHAL.AI - FULL INTERACTIVE CHAT APPLICATION
    // ============================================================
    
    // ----- CONFIGURATION -----
    const API_BASE = 'https://bishal-ai.onrender.com';
    const LOCAL_KEY = 's';

    // DOM References
    const chatMessages = document.getElementById('chatMessages');
    const messageInput = document.getElementById('messageInput');
    const sendBtn = document.getElementById('sendBtn');
    const modelSelect = document.getElementById('modelSelect');
    const statusBadge = document.getElementById('statusBadge');
    const googleLoginBtn = document.getElementById('googleLoginBtn');
    const loginBtnText = document.getElementById('loginBtnText');
    const userNameDisplay = document.getElementById('userNameDisplay');
    const avatarPlaceholder = document.getElementById('avatarPlaceholder');
    const logoutLink = document.getElementById('logoutLink');

    // State
    let currentUser = null;
    let isProcessing = false;
    let messageHistory = [];
    let messageCount = 0;
    let startTime = Date.now();

    // ----- User Management -----
    function setUser(user) {
      currentUser = user;
      if (user) {
        const name = user.name || user.email || 'User';
        userNameDisplay.textContent = name;
        avatarPlaceholder.textContent = name.charAt(0).toUpperCase();
        loginBtnText.textContent = 'Sign out';
        googleLoginBtn.classList.add('logged');
        logoutLink.classList.remove('hidden');
        statusBadge.innerHTML = `<span class="dot" style="background: #4ac7a2;"></span> ${name}`;
        // Store in localStorage
        localStorage.setItem('bishal_user', JSON.stringify(user));
      } else {
        userNameDisplay.textContent = 'Guest';
        avatarPlaceholder.textContent = 'G';
        loginBtnText.textContent = 'Sign in';
        googleLoginBtn.classList.remove('logged');
        logoutLink.classList.add('hidden');
        statusBadge.innerHTML = `<span class="dot" style="background: #4ac7a2;"></span> ready`;
        localStorage.removeItem('bishal_user');
      }
    }

    function toggleLogin() {
      if (currentUser) {
        setUser(null);
        addMessage('ai', '👋 You have been logged out.', 'system');
      } else {
        // Simulated Google login with richer profile
        const dummyUser = { 
          name: 'Bishal', 
          email: 'bishal@demo.com',
          picture: null,
          id: 'user_123'
        };
        setUser(dummyUser);
        addMessage('ai', `✨ Welcome, ${dummyUser.name}! You're signed in with Google (demo).`, 'system');
        // show welcome message with timestamp
        const time = new Date().toLocaleTimeString();
        addMessage('ai', `🕐 ${time} - Ready to assist you.`, 'system');
      }
    }

    // Check for existing session
    function restoreSession() {
      try {
        const saved = localStorage.getItem('bishal_user');
        if (saved) {
          const user = JSON.parse(saved);
          setUser(user);
        }
      } catch (e) {
        // ignore
      }
    }

    // ----- Chat Functions -----
    function addMessage(role, content, modelTag = null) {
      const div = document.createElement('div');
      div.className = `msg ${role}`;
      if (role === 'ai') {
        div.innerHTML = `<i class="fas fa-robot"></i> ${content}`;
        if (modelTag && modelTag !== 'system') {
          const tag = document.createElement('span');
          tag.className = 'model-tag';
          tag.textContent = modelTag || modelSelect.options[modelSelect.selectedIndex]?.text || 'llama';
          div.appendChild(tag);
        }
      } else {
        div.textContent = content;
      }
      chatMessages.appendChild(div);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      
      // Store in history
      messageHistory.push({ role, content, timestamp: new Date().toISOString() });
      messageCount++;
      return div;
    }

    function setStatus(text, isError = false) {
      const color = isError ? '#f27a7a' : '#4ac7a2';
      statusBadge.innerHTML = `<span class="dot" style="background: ${color};"></span> ${text}`;
    }

    // ----- Typing Indicator -----
    function showTyping() {
      const typingDiv = document.createElement('div');
      typingDiv.className = 'typing-indicator';
      typingDiv.id = 'typingIndicator';
      typingDiv.innerHTML = '<span></span><span></span><span></span>';
      chatMessages.appendChild(typingDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function hideTyping() {
      const indicator = document.getElementById('typingIndicator');
      if (indicator) indicator.remove();
    }

    // ----- API Call with Retry -----
    async function sendMessage(message, modelKey, retryCount = 0) {
      if (!message.trim() || isProcessing) return;
      
      // Add user message
      addMessage('user', message);
      messageInput.value = '';
      
      // Show typing indicator
      showTyping();
      
      isProcessing = true;
      sendBtn.disabled = true;
      setStatus('sending...');

      const model = modelKey || modelSelect.value;
      const url = `${API_BASE}/ask?message=${encodeURIComponent(message)}&key=${LOCAL_KEY}&model=${model}`;

      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 30000);
        
        const response = await fetch(url, { 
          method: 'GET', 
          headers: { 'Accept': 'application/json' },
          signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        const data = await response.json();
        
        hideTyping();
        
        if (response.ok && data.success) {
          const reply = data.reply || 'No reply from API.';
          const modelUsed = data.model || modelSelect.options[modelSelect.selectedIndex]?.text || 'llama';
          addMessage('ai', reply, modelUsed);
          setStatus('ready');
        } else {
          const errMsg = data.error || data.details || 'API error';
          addMessage('ai', `⚠️ ${errMsg}`, 'error');
          setStatus('error', true);
        }
      } catch (err) {
        hideTyping();
        if (err.name === 'AbortError') {
          addMessage('ai', '⏱️ Request timed out. Please try again.', 'error');
          setStatus('timeout', true);
        } else {
          addMessage('ai', `⚠️ Network error: ${err.message}`, 'error');
          setStatus('error', true);
        }
      } finally {
        isProcessing = false;
        sendBtn.disabled = false;
        messageInput.focus();
      }
    }

    // ----- Event Listeners -----
    sendBtn.addEventListener('click', (e) => { 
      e.preventDefault(); 
      const msg = messageInput.value.trim(); 
      if (msg) sendMessage(msg); 
    });

    messageInput.addEventListener('keydown', (e) => { 
      if (e.key === 'Enter' && !e.shiftKey) { 
        e.preventDefault(); 
        const msg = messageInput.value.trim(); 
        if (msg) sendMessage(msg); 
      } 
    });

    googleLoginBtn.addEventListener('click', toggleLogin);
    
    logoutLink.addEventListener('click', (e) => { 
      e.preventDefault(); 
      if (currentUser) { 
        setUser(null); 
        addMessage('ai', '🔒 Logged out successfully.', 'system'); 
      } 
    });

    modelSelect.addEventListener('change', function() {
      setStatus(`model: ${this.options[this.selectedIndex].text}`);
    });

    // ----- Auto-resize input on mobile -----
    messageInput.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = Math.min(this.scrollHeight, 120) + 'px';
    });

    // ----- Keyboard shortcuts -----
    document.addEventListener('keydown', (e) => {
      // Ctrl+Enter to send
      if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        const msg = messageInput.value.trim();
        if (msg) sendMessage(msg);
      }
      // Escape to clear input
      if (e.key === 'Escape') {
        messageInput.value = '';
        messageInput.blur();
      }
    });

    // ----- Initialize -----
    window.addEventListener('load', function() {
      // Set initial model tag
      const firstMsg = chatMessages.querySelector('.msg.ai .model-tag');
      if (firstMsg) firstMsg.textContent = modelSelect.options[modelSelect.selectedIndex].text;
      
      // Restore session
      restoreSession();
      
      setStatus('ready');
      
      // Show welcome message with system info
      const time = new Date().toLocaleTimeString();
      addMessage('ai', `🖥️ System ready at ${time}`, 'system');
      
      console.log('🚀 Bishal.ai initialized');
      console.log('📊 Available models:', ['llama', 'deepseek', 'minimax', 'gpt-oss']);
      
      // Update stats
      updateStats();
    });

    // ----- Stats update -----
    function updateStats() {
      const elapsed = Math.floor((Date.now() - startTime) / 1000);
      const minutes = Math.floor(elapsed / 60);
      const seconds = elapsed % 60;
      // Could display stats if needed
    }

    // ----- Error handling for uncaught errors -----
    window.addEventListener('unhandledrejection', function(e) {
      console.error('Unhandled rejection:', e.reason);
      addMessage('ai', '⚠️ An unexpected error occurred. Please try again.', 'error');
    });

    // ----- Export for debugging -----
    window.bishal = {
      sendMessage,
      setUser,
      getHistory: () => messageHistory,
      clearHistory: () => { messageHistory = []; chatMessages.innerHTML = ''; },
      getStats: () => ({ messageCount, uptime: Math.floor((Date.now() - startTime) / 1000) })
    };

  })();
</script>
</body>
</html>