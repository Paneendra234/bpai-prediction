import os
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.utils import timezone
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.platypus import KeepTogether
from io import BytesIO
from prediction.models import Prediction
from diet.models import DietPlan
from .models import HealthReport

@login_required
def generate_report(request, pk):
    pred = get_object_or_404(Prediction, pk=pk, user=request.user)
    diet_plan = DietPlan.objects.filter(prediction=pred).first()
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    styles = getSampleStyleSheet()
    story = []
    
    # Colors
    primary = colors.HexColor('#0d6efd')
    success = colors.HexColor('#198754')
    danger = colors.HexColor('#dc3545')
    warning = colors.HexColor('#ffc107')
    light_bg = colors.HexColor('#f8f9fa')
    dark = colors.HexColor('#212529')
    
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, textColor=primary, spaceAfter=6, fontName='Helvetica-Bold')
    heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], fontSize=14, textColor=primary, spaceBefore=12, spaceAfter=6, fontName='Helvetica-Bold')
    normal_style = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=10, textColor=dark, spaceAfter=4)
    sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#6c757d'), spaceAfter=3)
    
    # Header
    story.append(Paragraph("🏥 HealthMate AI", title_style))
    story.append(Paragraph("AI-Based Diabetes Prediction & Diet Recommendation Report", sub_style))
    story.append(HRFlowable(width="100%", thickness=2, color=primary))
    story.append(Spacer(1, 0.3*inch))
    
    # Patient Info
    story.append(Paragraph("📋 Patient Information", heading_style))
    patient_data = [
        ['Field', 'Details'],
        ['Patient Name', pred.user.get_full_name()],
        ['Username', pred.user.username],
        ['Email', pred.user.email or 'N/A'],
        ['Phone', pred.user.phone or 'N/A'],
        ['Report Date', pred.created_at.strftime('%B %d, %Y %I:%M %p')],
        ['Report ID', f'HM-{pred.pk:06d}'],
    ]
    patient_table = Table(patient_data, colWidths=[3*cm, 12*cm])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [light_bg, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dee2e6')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(patient_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Medical Parameters
    story.append(Paragraph("🔬 Medical Parameters", heading_style))
    params_data = [
        ['Parameter', 'Value', 'Unit', 'Reference Range'],
        ['Pregnancies', str(pred.pregnancies), 'Count', '0-17'],
        ['Glucose', str(pred.glucose), 'mg/dL', '70-99 (Normal)'],
        ['Blood Pressure', str(pred.blood_pressure), 'mmHg', '60-80 (Normal)'],
        ['Skin Thickness', str(pred.skin_thickness), 'mm', '10-50'],
        ['Insulin', str(pred.insulin), 'mu U/ml', '16-166 (2-hr serum)'],
        ['BMI', str(pred.bmi), 'kg/m²', '18.5-24.9 (Normal)'],
        ['Diabetes Pedigree', str(pred.diabetes_pedigree), 'Function', '< 0.5 (Lower risk)'],
        ['Age', str(pred.age), 'Years', '-'],
    ]
    params_table = Table(params_data, colWidths=[4*cm, 3*cm, 3*cm, 5*cm])
    params_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [light_bg, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dee2e6')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (1,1), (2,-1), 'CENTER'),
    ]))
    story.append(params_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Prediction Result
    story.append(Paragraph("🎯 Prediction Result", heading_style))
    result_color = danger if pred.prediction == 'Diabetic' else success
    result_data = [
        ['Diagnosis', 'Risk Score', 'Model Used'],
        [pred.prediction, f'{pred.risk_score}%', pred.model_used],
    ]
    result_table = Table(result_data, colWidths=[5*cm, 5*cm, 5*cm])
    result_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (0,1), (0,1), result_color),
        ('TEXTCOLOR', (0,1), (0,1), colors.white),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dee2e6')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('ROWHEIGHTS', (0,0), (-1,-1), 0.4*inch),
    ]))
    story.append(result_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Health Analysis
    story.append(Paragraph("💊 Health Analysis", heading_style))
    sugar_status, _ = pred.get_sugar_status()
    bp_status, _ = pred.get_bp_status()
    bmi_status, _ = pred.get_bmi_status()
    health_data = [
        ['Parameter', 'Value', 'Status'],
        ['Blood Sugar (Glucose)', f'{pred.glucose} mg/dL', sugar_status],
        ['Blood Pressure', f'{pred.blood_pressure} mmHg', bp_status],
        ['BMI', f'{pred.bmi} kg/m²', bmi_status],
    ]
    health_table = Table(health_data, colWidths=[5*cm, 5*cm, 5*cm])
    health_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [light_bg, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dee2e6')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (1,1), (-1,-1), 'CENTER'),
    ]))
    story.append(health_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Diet Plan
    if diet_plan and diet_plan.recommendation:
        rec = diet_plan.recommendation
        story.append(Paragraph("🥗 Personalized Diet Recommendations", heading_style))
        
        if rec.get('breakfast'):
            story.append(Paragraph("🌅 Breakfast Options", ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, textColor=success)))
            for item in rec['breakfast']:
                story.append(Paragraph(f"  • {item}", normal_style))
        
        if rec.get('lunch'):
            story.append(Paragraph("☀️ Lunch Options", ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, textColor=success)))
            for item in rec['lunch']:
                story.append(Paragraph(f"  • {item}", normal_style))
        
        if rec.get('dinner'):
            story.append(Paragraph("🌙 Dinner Options", ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, textColor=success)))
            for item in rec['dinner']:
                story.append(Paragraph(f"  • {item}", normal_style))
        
        if rec.get('tips'):
            story.append(Paragraph("💡 Health Tips", ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, textColor=warning)))
            for tip in rec['tips']:
                story.append(Paragraph(f"  • {tip}", normal_style))
    
    # Disclaimer
    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#dee2e6')))
    story.append(Spacer(1, 0.1*inch))
    disclaimer = ParagraphStyle('Disclaimer', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#6c757d'), alignment=1)
    story.append(Paragraph(
        "⚠️ DISCLAIMER: This report is generated by an AI system for informational purposes only. "
        "It is NOT a substitute for professional medical advice, diagnosis, or treatment. "
        "Please consult a qualified healthcare provider for medical decisions.",
        disclaimer
    ))
    story.append(Paragraph(f"Generated by HealthMate AI | {timezone.now().strftime('%B %d, %Y')}", disclaimer))
    
    doc.build(story)
    buffer.seek(0)
    
    filename = f"HealthMate_Report_{pred.user.username}_{pred.pk}.pdf"
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
