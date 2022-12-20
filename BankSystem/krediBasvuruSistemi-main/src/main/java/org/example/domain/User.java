package org.example.domain;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;


@Entity
@Table(name = "user")
public class User implements Cloneable{

	public User() {

	}

	public User(String name, String phone, Long identity, Long creditScore, Long inCome,Long creditAmount, Boolean creditStatus) {

		this.setName(name);
		this.setPhone(phone);
		this.setCreditScore(creditScore);
		this.setIdentity(identity);
		this.setInCome(inCome);
		this.setCreditStatus(creditStatus);
		this.setCreditAmount(creditAmount);

	}

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(name = "id", unique = true, nullable = false)
	private Long id;

	private String name;

	private Long identity;

	private String phone;

	private Long inCome;

	private Long creditScore;

	private Long creditAmount;

	private Boolean creditStatus;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Long getIdentity() {
		return identity;
	}

	public void setIdentity(Long identity) {
		this.identity = identity;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public Long getInCome() {
		return inCome;
	}

	public void setInCome(Long inCome) {
		this.inCome = inCome;
	}

	public Long getCreditScore() {
		return creditScore;
	}

	public void setCreditScore(Long creditScore) {
		this.creditScore = creditScore;
	}

	public Long getCreditAmount() {
		return creditAmount;
	}

	public void setCreditAmount(Long creditAmount) {
		this.creditAmount = creditAmount;
	}

	public Boolean getCreditStatus() {
		return creditStatus;
	}

	public void setCreditStatus(Boolean creditStatus) {
		this.creditStatus = creditStatus;
	}
}