// ==================== Form Validation & Interactions ====================

// Train Model Function
async function trainModel() {
    const trainButton = document.getElementById('trainButton');
    const trainingStatus = document.getElementById('trainingStatus');
    const statusMessage = document.getElementById('statusMessage');
    const statusDetails = document.getElementById('statusDetails');
    
    // Get loader element
    const loader = trainingStatus.querySelector('.loader');
    
    // Disable button and show loading
    trainButton.disabled = true;
    trainButton.innerHTML = '<div class="loading"></div> Training...';
    
    // Show training status
    trainingStatus.style.display = 'block';
    trainingStatus.className = 'training-status';
    statusMessage.textContent = 'Training in progress...';
    statusDetails.textContent = 'Please wait, this may take a few minutes (typically 2-5 minutes)';
    
    // Make sure loader is visible
    if (loader) {
        loader.classList.remove('hidden');
    }
    
    try {
        const response = await fetch('/train', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            // Success - HIDE LOADER
            if (loader) {
                loader.classList.add('hidden');
            }
            
            trainingStatus.className = 'training-status status-success';
            statusMessage.textContent = data.message;
            statusDetails.textContent = data.details;
            trainButton.innerHTML = '<span class="btn-icon">✅</span> Training Complete!';
            
            showNotification('Model trained successfully! You can now make predictions.', 'success');
            
            // Scroll to prediction form
            setTimeout(() => {
                document.querySelector('.form-container').scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 1500);
            
        } else {
            // Error - HIDE LOADER
            if (loader) {
                loader.classList.add('hidden');
            }
            
            trainingStatus.className = 'training-status status-error';
            statusMessage.textContent = data.message;
            statusDetails.textContent = data.details;
            trainButton.innerHTML = '<span class="btn-icon">🚀</span> Start Training';
            trainButton.disabled = false;
            
            showNotification('Training failed. Please try again.', 'error');
        }
        
    } catch (error) {
        // Network or other error - HIDE LOADER
        if (loader) {
            loader.classList.add('hidden');
        }
        
        trainingStatus.className = 'training-status status-error';
        statusMessage.textContent = 'Training Failed ❌';
        statusDetails.textContent = `Error: ${error.message}`;
        trainButton.innerHTML = '<span class="btn-icon">🚀</span> Start Training';
        trainButton.disabled = false;
        
        showNotification('Network error. Please check your connection and try again.', 'error');
    }
}

// Reset form function
function resetForm() {
    document.getElementById('predictionForm').reset();
    
    // Hide result container if visible
    const resultContainer = document.getElementById('resultContainer');
    if (resultContainer) {
        resultContainer.style.display = 'none';
    }
    
    // Show success message
    showNotification('Form reset successfully!', 'info');
}

// Fill example data function
function fillExample() {
    // Example of a good quality wine
    const exampleData = {
        fixed_acidity: 7.4,
        volatile_acidity: 0.70,
        citric_acid: 0.00,
        residual_sugar: 1.9,
        chlorides: 0.076,
        free_sulfur_dioxide: 11.0,
        total_sulfur_dioxide: 34.0,
        density: 0.9978,
        pH: 3.51,
        sulphates: 0.56,
        alcohol: 9.4
    };
    
    // Fill form with example data
    Object.keys(exampleData).forEach(key => {
        const input = document.getElementById(key);
        if (input) {
            input.value = exampleData[key];
            
            // Add animation
            input.style.transition = 'all 0.3s ease';
            input.style.background = '#e8f5e9';
            setTimeout(() => {
                input.style.background = '#f8f9fa';
            }, 500);
        }
    });
    
    showNotification('Example data loaded! Click Predict to see the result.', 'success');
}

// Show notification
function showNotification(message, type = 'info') {
    // Remove existing notification if any
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Notification styles
    const notificationStyles = {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '15px 25px',
        borderRadius: '10px',
        color: 'white',
        fontWeight: '500',
        zIndex: '9999',
        boxShadow: '0 4px 20px rgba(0,0,0,0.2)',
        animation: 'slideInRight 0.3s ease',
        maxWidth: '400px'
    };
    
    Object.assign(notification.style, notificationStyles);
    
    // Set background color based on type
    const colors = {
        success: '#4CAF50',
        error: '#f44336',
        info: '#2196F3',
        warning: '#ff9800'
    };
    notification.style.background = colors[type] || colors.info;
    
    // Add to body
    document.body.appendChild(notification);
    
    // Remove after 4 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 4000);
}

// Add CSS animations dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Form submission handling
document.getElementById('predictionForm').addEventListener('submit', function(e) {
    const submitButton = this.querySelector('.btn-predict');
    const originalText = submitButton.innerHTML;
    
    // Show loading state
    submitButton.innerHTML = '<div class="loading"></div> Predicting...';
    submitButton.disabled = true;
    
    // Validate all inputs
    const inputs = this.querySelectorAll('input[type="number"]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value) {
            isValid = false;
            input.style.borderColor = '#f44336';
        } else {
            input.style.borderColor = '#e0e0e0';
        }
    });
    
    if (!isValid) {
        e.preventDefault();
        submitButton.innerHTML = originalText;
        submitButton.disabled = false;
        showNotification('Please fill in all fields!', 'error');
    }
});

// Input validation on change
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', function() {
        if (this.value) {
            this.style.borderColor = '#4CAF50';
        } else {
            this.style.borderColor = '#e0e0e0';
        }
    });
    
    // Add focus effect
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.02)';
        this.parentElement.style.transition = 'transform 0.2s ease';
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
    });
});

// Smooth scroll to result
if (document.getElementById('resultContainer')) {
    setTimeout(() => {
        document.getElementById('resultContainer').scrollIntoView({ 
            behavior: 'smooth',
            block: 'center'
        });
    }, 100);
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + R to reset form
    if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
        e.preventDefault();
        resetForm();
    }
    
    // Ctrl/Cmd + E to load example
    if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
        e.preventDefault();
        fillExample();
    }
    
    // Ctrl/Cmd + T to train model
    if ((e.ctrlKey || e.metaKey) && e.key === 't') {
        e.preventDefault();
        trainModel();
    }
});

// Show keyboard shortcuts on page load
window.addEventListener('load', function() {
    setTimeout(() => {
        showNotification('💡 Tip: Train model first (Step 1), then make predictions! Press Ctrl+T to train.', 'info');
    }, 1000);
});

console.log('🍷 Wine Quality Predictor initialized successfully!');
console.log('📝 Keyboard shortcuts: Ctrl+T (Train), Ctrl+E (Example), Ctrl+R (Reset)');
