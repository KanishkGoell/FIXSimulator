<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FIX Trading Gateway Simulator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #ffffff;
            min-height: 100vh;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #ffd700, #ffed4e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }

        .panel {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .panel h3 {
            margin-bottom: 15px;
            color: #ffd700;
            font-size: 1.2em;
        }

        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }

        .status-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .status-value {
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
        }

        .status-label {
            font-size: 0.9em;
            opacity: 0.8;
            margin-top: 5px;
        }

        .client-list {
            max-height: 300px;
            overflow-y: auto;
        }

        .client-item {
            background: rgba(255, 255, 255, 0.05);
            margin-bottom: 10px;
            padding: 15px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .client-status {
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
        }

        .status-connected {
            background: #4CAF50;
            color: white;
        }

        .status-disconnected {
            background: #f44336;
            color: white;
        }

        .controls {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }

        .control-section {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #ffd700;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 14px;
        }

        .form-group input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        .btn {
            background: linear-gradient(45deg, #ffd700, #ffed4e);
            color: #1e3c72;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
        }

        .message-log {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            padding: 20px;
            height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }

        .message-item {
            margin-bottom: 10px;
            padding: 8px;
            border-radius: 5px;
            border-left: 4px solid;
        }

        .message-incoming {
            background: rgba(76, 175, 80, 0.1);
            border-left-color: #4CAF50;
        }

        .message-outgoing {
            background: rgba(33, 150, 243, 0.1);
            border-left-color: #2196F3;
        }

        .message-error {
            background: rgba(244, 67, 54, 0.1);
            border-left-color: #f44336;
        }

        .timestamp {
            color: #ffd700;
            font-size: 0.8em;
        }

        .latency-chart {
            height: 200px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
            position: relative;
            overflow: hidden;
        }

        .chart-bars {
            display: flex;
            align-items: end;
            height: 100%;
            gap: 2px;
        }

        .chart-bar {
            background: linear-gradient(to top, #4CAF50, #81C784);
            min-width: 8px;
            border-radius: 2px 2px 0 0;
            transition: height 0.3s ease;
        }

        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .controls {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>FIX Trading Gateway Simulator</h1>
            <p>Professional Electronic Trading System with Real-time Monitoring</p>
        </div>

        <div class="dashboard">
            <div class="panel">
                <h3>System Status</h3>
                <div class="status-grid">
                    <div class="status-card">
                        <div class="status-value" id="activeClients">0</div>
                        <div class="status-label">Active Clients</div>
                    </div>
                    <div class="status-card">
                        <div class="status-value" id="totalOrders">0</div>
                        <div class="status-label">Total Orders</div>
                    </div>
                    <div class="status-card">
                        <div class="status-value" id="avgLatency">0ms</div>
                        <div class="status-label">Avg Latency</div>
                    </div>
                    <div class="status-card">
                        <div class="status-value" id="systemUptime">00:00:00</div>
                        <div class="status-label">Uptime</div>
                    </div>
                </div>
                
                <h4 style="color: #ffd700; margin-bottom: 10px;">Latency Chart (Last 50 Messages)</h4>
                <div class="latency-chart">
                    <div class="chart-bars" id="latencyChart"></div>
                </div>
            </div>

            <div class="panel">
                <h3>Connected Clients</h3>
                <div class="client-list" id="clientList">
                    <!-- Client connections will be populated here -->
                </div>
            </div>
        </div>

        <div class="controls">
            <div class="control-section">
                <h3 style="color: #ffd700; margin-bottom: 15px;">Client Management</h3>
                <div class="form-group">
                    <label>Client ID</label>
                    <input type="text" id="clientId" placeholder="e.g., GOLDMAN_CLIENT_01">
                </div>
                <div class="form-group">
                    <label>Sender Comp ID</label>
                    <input type="text" id="senderCompId" placeholder="e.g., GSCO">
                </div>
                <div class="form-group">
                    <label>Target Comp ID</label>
                    <input type="text" id="targetCompId" placeholder="e.g., CLIENT">
                </div>
                <button class="btn" onclick="connectClient()">Connect Client</button>
            </div>

            <div class="control-section">
                <h3 style="color: #ffd700; margin-bottom: 15px;">Order Simulation</h3>
                <div class="form-group">
                    <label>Symbol</label>
                    <input type="text" id="symbol" placeholder="e.g., AAPL" value="AAPL">
                </div>
                <div class="form-group">
                    <label>Side</label>
                    <select id="side">
                        <option value="1">Buy</option>
                        <option value="2">Sell</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Quantity</label>
                    <input type="number" id="quantity" placeholder="100" value="100">
                </div>
                <div class="form-group">
                    <label>Price</label>
                    <input type="number" id="price" placeholder="150.00" value="150.00" step="0.01">
                </div>
                <button class="btn" onclick="sendOrder()">Send Order</button>
            </div>

            <div class="control-section">
                <h3 style="color: #ffd700; margin-bottom: 15px;">System Controls</h3>
                <div class="form-group">
                    <label>Simulation Speed</label>
                    <select id="simSpeed">
                        <option value="1000">Slow (1s)</option>
                        <option value="500" selected>Normal (0.5s)</option>
                        <option value="100">Fast (0.1s)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Auto-Execute Orders</label>
                    <select id="autoExecute">
                        <option value="true" selected>Enabled</option>
                        <option value="false">Disabled</option>
                    </select>
                </div>
                <button class="btn" onclick="clearLogs()">Clear Logs</button>
                <button class="btn" onclick="resetSystem()" style="margin-top: 10px; background: linear-gradient(45deg, #f44336, #e57373);">Reset System</button>
            </div>
        </div>

        <div class="panel">
            <h3>FIX Message Log</h3>
            <div class="message-log" id="messageLog">
                <div class="message-item message-incoming">
                    <span class="timestamp">[2025-07-29 12:00:00]</span> 
                    <strong>INCOMING:</strong> 8=FIX.4.2|9=178|35=A|49=CLIENT|56=GSCO|34=1|52=20250729-12:00:00|98=0|108=30|10=123|
                </div>
                <div class="message-item message-outgoing">
                    <span class="timestamp">[2025-07-29 12:00:00]</span> 
                    <strong>OUTGOING:</strong> 8=FIX.4.2|9=165|35=A|49=GSCO|56=CLIENT|34=1|52=20250729-12:00:00|98=0|108=30|10=456|
                </div>
            </div>
        </div>
    </div>

    <script>
        // FIX Protocol Trading Gateway Simulator
        class FIXTradingGateway {
            constructor() {
                this.clients = new Map();
                this.orders = [];
                this.messageLog = [];
                this.latencyData = [];
                this.sequenceNumbers = new Map();
                this.systemStartTime = Date.now();
                this.totalOrderCount = 0;
                
                this.initializeSystem();
                this.startSystemMonitoring();
            }

            initializeSystem() {
                this.updateDisplay();
                this.addSystemMessage("System initialized and ready for connections", "incoming");
            }

            // FIX Message Generation
            generateFIXMessage(msgType, senderCompId, targetCompId, fields = {}) {
                const timestamp = new Date().toISOString().replace(/[-:]/g, '').split('.')[0];
                const seqNum = this.getNextSequenceNumber(senderCompId);
                
                let message = `8=FIX.4.2|9=000|35=${msgType}|49=${senderCompId}|56=${targetCompId}|34=${seqNum}|52=${timestamp}|`;
                
                // Add custom fields
                Object.entries(fields).forEach(([tag, value]) => {
                    message += `${tag}=${value}|`;
                });

                // Calculate body length (simplified)
                const bodyLength = message.split('|').slice(2, -1).join('|').length;
                message = message.replace('9=000', `9=${bodyLength.toString().padStart(3, '0')}`);
                
                // Add checksum (simplified)
                const checksum = Math.floor(Math.random() * 256).toString().padStart(3, '0');
                message += `10=${checksum}|`;
                
                return message;
            }

            getNextSequenceNumber(compId) {
                if (!this.sequenceNumbers.has(compId)) {
                    this.sequenceNumbers.set(compId, 1);
                } else {
                    this.sequenceNumbers.set(compId, this.sequenceNumbers.get(compId) + 1);
                }
                return this.sequenceNumbers.get(compId);
            }

            // Client Management
            connectClient(clientId, senderCompId, targetCompId) {
                if (this.clients.has(clientId)) {
                    this.addSystemMessage(`Client ${clientId} already connected`, "error");
                    return false;
                }

                const client = {
                    clientId,
                    senderCompId,
                    targetCompId,
                    connected: true,
                    connectTime: Date.now(),
                    lastHeartbeat: Date.now(),
                    orderCount: 0
                };

                this.clients.set(clientId, client);
                
                // Send logon acknowledgment
                const logonAck = this.generateFIXMessage('A', targetCompId, senderCompId, {
                    '98': '0',
                    '108': '30'
                });
                
                this.addMessageToLog(logonAck, "outgoing", `Logon ACK to ${clientId}`);
                this.updateDisplay();
                
                return true;
            }

            disconnectClient(clientId) {
                if (this.clients.has(clientId)) {
                    const client = this.clients.get(clientId);
                    
                    // Send logout message
                    const logout = this.generateFIXMessage('5', client.targetCompId, client.senderCompId, {
                        '58': 'Logout initiated by server'
                    });
                    
                    this.addMessageToLog(logout, "outgoing", `Logout to ${clientId}`);
                    this.clients.delete(clientId);
                    this.updateDisplay();
                }
            }

            // Order Processing
            processOrder(symbol, side, quantity, price, clientId = 'DEFAULT_CLIENT') {
                const orderId = `ORD${Date.now()}${Math.floor(Math.random() * 1000)}`;
                const clOrdId = `CLO${Date.now()}${Math.floor(Math.random() * 1000)}`;
                
                const order = {
                    orderId,
                    clOrdId,
                    symbol,
                    side,
                    quantity: parseInt(quantity),
                    price: parseFloat(price),
                    clientId,
                    timestamp: Date.now(),
                    status: 'NEW'
                };

                this.orders.push(order);
                this.totalOrderCount++;

                // Generate New Order Single message
                const newOrderMsg = this.generateFIXMessage('D', 'CLIENT', 'GSCO', {
                    '11': clOrdId,
                    '21': '1',
                    '55': symbol,
                    '54': side,
                    '38': quantity,
                    '40': '2',
                    '44': price,
                    '60': new Date().toISOString().replace(/[-:]/g, '').split('.')[0]
                });

                this.addMessageToLog(newOrderMsg, "incoming", `New Order from ${clientId}`);

                // Auto-execute if enabled
                if (document.getElementById('autoExecute').value === 'true') {
                    setTimeout(() => this.executeOrder(order), parseInt(document.getElementById('simSpeed').value));
                }

                // Update client order count
                if (this.clients.has(clientId)) {
                    this.clients.get(clientId).orderCount++;
                }

                this.updateDisplay();
                return order;
            }

            executeOrder(order) {
                const executionId = `EXEC${Date.now()}${Math.floor(Math.random() * 1000)}`;
                const latency = Math.floor(Math.random() * 50) + 5; // 5-55ms latency
                
                this.latencyData.push(latency);
                if (this.latencyData.length > 50) {
                    this.latencyData.shift();
                }

                // Generate Execution Report
                const execReport = this.generateFIXMessage('8', 'GSCO', 'CLIENT', {
                    '37': order.orderId,
                    '11': order.clOrdId,
                    '17': executionId,
                    '20': '0',
                    '39': '2', // Filled
                    '55': order.symbol,
                    '54': order.side,
                    '38': order.quantity,
                    '32': order.quantity,
                    '31': order.price,
                    '60': new Date().toISOString().replace(/[-:]/g, '').split('.')[0]
                });

                this.addMessageToLog(execReport, "outgoing", `Execution Report for ${order.clOrdId} (${latency}ms)`);
                
                order.status = 'FILLED';
                order.executionTime = Date.now();
                order.latency = latency;

                this.updateDisplay();
            }

            // Message Logging
            addMessageToLog(message, direction, description = '') {
                const timestamp = new Date().toLocaleString();
                const logEntry = {
                    timestamp,
                    message,
                    direction,
                    description
                };
                
                this.messageLog.push(logEntry);
                
                const messageLogDiv = document.getElementById('messageLog');
                const messageItem = document.createElement('div');
                messageItem.className = `message-item message-${direction}`;
                messageItem.innerHTML = `
                    <span class="timestamp">[${timestamp}]</span> 
                    <strong>${direction.toUpperCase()}:</strong> ${message}
                    ${description ? `<br><small style="opacity: 0.7;">${description}</small>` : ''}
                `;
                
                messageLogDiv.appendChild(messageItem);
                messageLogDiv.scrollTop = messageLogDiv.scrollHeight;
                
                // Keep only last 100 messages
                if (this.messageLog.length > 100) {
                    this.messageLog.shift();
                    messageLogDiv.removeChild(messageLogDiv.firstChild);
                }
            }

            addSystemMessage(message, type = "incoming") {
                this.addMessageToLog(`SYSTEM: ${message}`, type);
            }

            // Display Updates
            updateDisplay() {
                document.getElementById('activeClients').textContent = this.clients.size;
                document.getElementById('totalOrders').textContent = this.totalOrderCount;
                
                const avgLatency = this.latencyData.length > 0 
                    ? Math.round(this.latencyData.reduce((a, b) => a + b, 0) / this.latencyData.length)
                    : 0;
                document.getElementById('avgLatency').textContent = `${avgLatency}ms`;

                this.updateClientList();
                this.updateLatencyChart();
            }

            updateClientList() {
                const clientListDiv = document.getElementById('clientList');
                clientListDiv.innerHTML = '';
                
                if (this.clients.size === 0) {
                    clientListDiv.innerHTML = '<div style="text-align: center; opacity: 0.7;">No clients connected</div>';
                    return;
                }

                this.clients.forEach((client, clientId) => {
                    const clientItem = document.createElement('div');
                    clientItem.className = 'client-item';
                    clientItem.innerHTML = `
                        <div>
                            <strong>${clientId}</strong><br>
                            <small>${client.senderCompId} → ${client.targetCompId}</small><br>
                            <small>Orders: ${client.orderCount}</small>
                        </div>
                        <div>
                            <span class="client-status status-connected">Connected</span>
                            <button onclick="gateway.disconnectClient('${clientId}')" style="margin-left: 10px; background: #f44336; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">Disconnect</button>
                        </div>
                    `;
                    clientListDiv.appendChild(clientItem);
                });
            }

            updateLatencyChart() {
                const chartDiv = document.getElementById('latencyChart');
                chartDiv.innerHTML = '';
                
                const maxLatency = Math.max(...this.latencyData, 60);
                
                this.latencyData.forEach(latency => {
                    const bar = document.createElement('div');
                    bar.className = 'chart-bar';
                    bar.style.height = `${(latency / maxLatency) * 100}%`;
                    bar.title = `${latency}ms`;
                    chartDiv.appendChild(bar);
                });
            }

            updateUptime() {
                const uptime = Date.now() - this.systemStartTime;
                const hours = Math.floor(uptime / (1000 * 60 * 60));
                const minutes = Math.floor((uptime % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((uptime % (1000 * 60)) / 1000);
                
                document.getElementById('systemUptime').textContent = 
                    `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            }

            startSystemMonitoring() {
                // Update uptime every second
                setInterval(() => {
                    this.updateUptime();
                }, 1000);

                // Send periodic heartbeats
                setInterval(() => {
                    this.clients.forEach((client, clientId) => {
                        const heartbeat = this.generateFIXMessage('0', client.targetCompId, client.senderCompId, {
                            '112': 'HEARTBEAT'
                        });
                        this.addMessageToLog(heartbeat, "outgoing", `Heartbeat to ${clientId}`);
                    });
                }, 30000); // Every 30 seconds

                // Simulate some market activity
                setInterval(() => {
                    if (this.clients.size > 0 && Math.random() > 0.7) {
                        const symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN'];
                        const symbol = symbols[Math.floor(Math.random() * symbols.length)];
                        const side = Math.random() > 0.5 ? '1' : '2';
                        const quantity = Math.floor(Math.random() * 1000) + 100;
                        const price = (Math.random() * 200 + 50).toFixed(2);
                        
                        const clientId = Array.from(this.clients.keys())[0];
                        this.processOrder(symbol, side, quantity, price, clientId);
                    }
                }, 5000); // Every 5 seconds
            }

            clearLogs() {
                document.getElementById('messageLog').innerHTML = '';
                this.messageLog = [];
                this.addSystemMessage("Message logs cleared");
            }

            resetSystem() {
                this.clients.clear();
                this.orders = [];
                this.messageLog = [];
                this.latencyData = [];
                this.sequenceNumbers.clear();
                this.totalOrderCount = 0;
                this.systemStartTime = Date.now();
                
                document.getElementById('messageLog').innerHTML = '';
                this.updateDisplay();
                this.addSystemMessage("System reset completed");
            }
        }

        // Initialize the gateway
        const gateway = new FIXTradingGateway();

        // UI Functions
        function connectClient() {
            const clientId = document.getElementById('clientId').value;
            const senderCompId = document.getElementById('senderCompId').value;
            const targetCompId = document.getElementById('targetCompId').value;
            
            if (!clientId || !senderCompId || !targetCompId) {
                alert('Please fill in all client connection fields');
                return;
            }
            
            if (gateway.connectClient(clientId, senderCompId, targetCompId)) {
                // Clear form
                document.getElementById('clientId').value = '';
                document.getElementById('senderCompId').value = '';
                document.getElementById('targetCompId').value = '';
            }
        }

        function sendOrder() {
            const symbol = document.getElementById('symbol').value;
            const side = document.getElementById('side').value;
            const quantity = document.getElementById('quantity').value;
            const price = document.getElementById('price').value;
            
            if (!symbol || !quantity || !price) {
                alert('Please fill in all order fields');
                return;
            }
            
            if (gateway.clients.size === 0) {
                alert('No clients connected. Please connect a client first.');
                return;
            }
            
            const clientId = Array.from(gateway.clients.keys())[0];
            gateway.processOrder(symbol, side, quantity, price, clientId);
        }

        function clearLogs() {
            gateway.clearLogs();
        }

        function resetSystem() {
            if (confirm('Are you sure you want to reset the entire system? This will disconnect all clients and clear all data.')) {
                gateway.resetSystem();
            }
        }

        // Auto-populate some demo data on load
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('clientId').value = 'GOLDMAN_CLIENT_01';
                document.getElementById('senderCompId').value = 'GSCO';
                document.getElementById('targetCompId').value = 'CLIENT';
            }, 1000);
        });
    </script>
</body>
</html>
